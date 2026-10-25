#!/usr/bin/env python3
"""Create, draw and check a project's structure from docs/structure.yml.

Run from the project repository root:
  python3 <skills>/project-flow/scripts/structure.py init --name "My project" --skills .claude/skills
  python3 <skills>/project-flow/scripts/structure.py render   # redraw the tree in docs/README.md
  python3 <skills>/project-flow/scripts/structure.py check    # exit 1 if anything in docs/ is misplaced

Standard library only. Uses PyYAML if installed, otherwise a built-in reader for the
simple format used by structure.yml.
"""
import argparse
import datetime
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATES = os.path.join(os.path.dirname(HERE), "templates")
SKILLS = os.path.dirname(os.path.dirname(HERE))
STRUCTURE = os.path.join("docs", "structure.yml")
BEGIN, END = "<!-- structure:begin -->", "<!-- structure:end -->"
DESC_COL = 29  # column where descriptions start in the drawn tree
ROOT_LABEL = "<project repo>/"


# ---------- reading structure.yml ----------

def _simple_yaml(text):
    """Read nested 'key: value' / 'key:' mappings indented with spaces."""
    root, stack = {}, [(-1, None)]
    stack[0] = (-1, root)
    for raw in text.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        line = raw.strip()
        key, _, value = line.partition(":")
        key, value = key.strip(), value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        while stack[-1][0] >= indent:
            stack.pop()
        parent = stack[-1][1]
        if value == "":
            parent[key] = {}
            stack.append((indent, parent[key]))
        else:
            parent[key] = int(value) if value.isdigit() else value
    return root


def load(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    try:
        import yaml  # type: ignore
        data = yaml.safe_load(text)
    except ImportError:
        data = _simple_yaml(text)
    return data["tree"]


def entries(tree):
    """Yield (name, description, children-or-None) in file order, skipping '_'."""
    for name, value in tree.items():
        if name == "_":
            continue
        if isinstance(value, dict):
            yield name, str(value.get("_", "")), value
        else:
            yield name, str(value), None


def is_placeholder(name):
    return "<" in name


def pattern(name):
    out = ""
    for part in re.split(r"(<[^>]+>)", name):
        if part.startswith("<"):
            out += r"[^/]+"
        else:
            out += "".join(r"\d" if c.isdigit() else re.escape(c) for c in part)
    return re.compile("^" + out + "$")


# ---------- render ----------

def draw(tree):
    lines = [ROOT_LABEL]

    def walk(node, prefix):
        items = list(entries(node))
        for i, (name, desc, children) in enumerate(items):
            last = i == len(items) - 1
            head = prefix + ("└── " if last else "├── ") + name
            pad = max(DESC_COL - len(head), 2)
            lines.append(head + " " * pad + desc if desc else head)
            if children is not None:
                walk(children, prefix + ("    " if last else "│   "))

    walk(tree, "")
    return "```\n" + "\n".join(lines) + "\n```"


def render(readme=os.path.join("docs", "README.md"), structure=STRUCTURE):
    block = BEGIN + "\n" + draw(load(structure)) + "\n" + END
    with open(readme, encoding="utf-8") as f:
        text = f.read()
    if BEGIN in text and END in text:
        text = text[: text.index(BEGIN)] + block + text[text.index(END) + len(END):]
    else:
        text = text.rstrip() + "\n\n" + block + "\n"
    with open(readme, "w", encoding="utf-8") as f:
        f.write(text)


# ---------- init ----------

def title_of(name):
    base = os.path.splitext(name)[0].replace("-", " ").replace("_", " ")
    return base[:1].upper() + base[1:]


OUTPUT = re.compile(r"^## Output: (\S+)\s*\n+```markdown\n(# .+)$", re.M)


def skill_headings():
    """Map each output path to the heading its skill's '## Output: <path>' block starts with."""
    headings = {}
    for dirpath, _, filenames in os.walk(SKILLS):
        for fn in filenames:
            if fn.endswith(".md"):
                with open(os.path.join(dirpath, fn), encoding="utf-8") as f:
                    headings.update(OUTPUT.findall(f.read()))
    return headings


def stub(path, desc, heading=None):
    heading = heading or "# " + title_of(os.path.basename(path))
    if path.startswith("docs/design/"):
        return (f"{heading}\nAudience: · Last updated: <date> by <name>\nSources:\n\n"
                f"> Status: not started. Holds: {desc}.\n")
    return f"{heading}\n\n> Status: not started. Holds: {desc}.\n"


def fill(text, values):
    for key, val in values.items():
        text = text.replace(key, val)
    return text


def author():
    """Git user name for 'Last updated by', or 'contributor' if none is set."""
    try:
        out = subprocess.run(["git", "config", "user.name"], capture_output=True, text=True)
    except OSError:
        return "contributor"
    return out.stdout.strip() or "contributor"


def init(name, skills):
    values = {"<Project name>": name, "<project name>": name, "<project>": name,
              "<skills>": skills.rstrip("/"), "<date>": datetime.date.today().isoformat(),
              "<name>": author()}
    created, kept, merged = [], [], []
    already = os.path.exists(os.path.join("docs", "STATE.md"))
    os.makedirs("docs", exist_ok=True)
    if not os.path.exists(STRUCTURE):
        shutil.copy(os.path.join(TEMPLATES, "structure.yml"), STRUCTURE)
        created.append(STRUCTURE)
    tree = load(STRUCTURE)
    headings = {p: fill(h, values) for p, h in skill_headings().items()}

    def template_for(path):
        special = {"AGENTS.md": "AGENTS.md", "CLAUDE.md": "CLAUDE.md",
                   "docs/README.md": "docs-README.md"}
        cand = os.path.join(TEMPLATES, special.get(path, os.path.join("files", path)))
        return cand if os.path.exists(cand) else None

    def walk(node, base):
        for entry, desc, children in entries(node):
            path = base + entry
            if is_placeholder(entry):
                continue  # patterns and <code>/ are not created
            if entry.endswith("/"):
                os.makedirs(path, exist_ok=True)
                if children is not None:
                    walk(children, path)
                elif not os.listdir(path):
                    open(os.path.join(path, ".gitkeep"), "w").close()
                    created.append(path)
                continue
            if path in created:
                continue
            tpl = template_for(path)
            content = fill(open(tpl, encoding="utf-8").read(), values) if tpl else fill(stub(path, desc, headings.get(path)), values)
            if not os.path.exists(path):
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)
                created.append(path)
            elif path in ("AGENTS.md", "CLAUDE.md"):
                old = open(path, encoding="utf-8").read()
                marker = "@AGENTS.md" if path == "CLAUDE.md" else "# Agent instructions: project workflow"
                if marker not in old:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(content.rstrip() + "\n\n" + old)
                    merged.append(path)
                else:
                    kept.append(path)
            else:
                kept.append(path)

    walk(tree, "")
    render()
    if "build/" in tree:
        # Keep build/ itself in git, never its generated snapshots.
        lines = ["build/*", "!build/.gitkeep"]
        old = open(".gitignore", encoding="utf-8").read() if os.path.exists(".gitignore") else None
        missing = [ln for ln in lines if ln not in (old or "").splitlines()]
        if missing:
            with open(".gitignore", "a", encoding="utf-8") as f:
                if old and not old.endswith("\n"):
                    f.write("\n")
                f.write("\n".join(missing) + "\n")
            (created if old is None else merged).append(".gitignore")
    for label, items in (("created", created), ("merged (workflow content added to an existing file)", merged),
                         ("kept (already existed)", kept)):
        if items:
            print(f"{label}:")
            for p in items:
                print("  " + p)
    if already:
        print("Project already set up; nothing was overwritten and --name was not applied.")


# ---------- check ----------

SECRET = re.compile(r"(AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY-----|"
                    r"(?i:(api[_-]?key|secret|password|token)\s*[:=]\s*['\"]?[A-Za-z0-9_\-/+]{16,}))")


def check():
    tree = load(STRUCTURE)
    errors, warnings = [], []

    def match(node, name, is_dir):
        same_kind = [(e, c) for e, _, c in entries(node) if e.endswith("/") == is_dir]
        for entry, children in same_kind:  # exact names win over placeholders
            if entry.rstrip("/") == name:
                return entry, children
        for entry, children in same_kind:
            if is_placeholder(entry) and pattern(entry.rstrip("/")).match(name):
                return entry, children
        return None, None

    def walk(node, base, real):
        for name in sorted(os.listdir(real)):
            if name.startswith("."):
                continue
            full = os.path.join(real, name)
            is_dir = os.path.isdir(full)
            entry, children = match(node, name, is_dir)
            rel = base + name + ("/" if is_dir else "")
            if entry is None:
                errors.append(f"not in structure.yml: {rel}")
                continue
            if is_dir and children is not None:
                walk(children, rel, full)
        for entry, _, _ in entries(node):
            if not is_placeholder(entry) and not os.path.exists(os.path.join(real, entry.rstrip("/"))):
                warnings.append(f"missing: {base}{entry}")

    # Only docs/ and the root files are checked; code folders and anything else
    # beside docs/ are left alone.
    docs_entry, docs_children = match(tree, "docs", True)
    if docs_children is not None and os.path.isdir("docs"):
        walk(docs_children, "docs/", "docs")
    for entry, _, _ in entries(tree):
        if not entry.endswith("/") and not os.path.exists(entry):
            warnings.append(f"missing: {entry}")

    for dirpath, dirnames, filenames in os.walk("docs"):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for fn in filenames:
            path = os.path.join(dirpath, fn).replace(os.sep, "/")
            if not fn.endswith((".md", ".yml", ".yaml", ".mmd", ".json")):
                continue
            text = open(path, encoding="utf-8", errors="ignore").read()
            if SECRET.search(text):
                errors.append(f"possible secret value: {path}")
            if path.startswith("docs/design/") and fn.endswith(".md") and "/api/" not in path:
                if "Last updated:" not in text:
                    warnings.append(f"missing Last updated header: {path}")

    for w in warnings:
        print("warning: " + w)
    for e in errors:
        print("error:   " + e)
    if errors:
        print(f"\n{len(errors)} error(s). See docs/README.md for where each file belongs; "
              "change the structure only through a decision record and docs/structure.yml.")
        return 1
    print("structure ok" + (f" ({len(warnings)} warning(s))" if warnings else ""))
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("init", help="create every file and folder in structure.yml")
    p.add_argument("--name", required=True, help="project name")
    p.add_argument("--skills", required=True, help="path where the workflow skills are installed")
    sub.add_parser("render", help="redraw the tree in docs/README.md from docs/structure.yml")
    sub.add_parser("check", help="report docs/ files that do not match docs/structure.yml")
    a = ap.parse_args()
    if a.cmd != "init" and not os.path.exists(STRUCTURE):
        print("No docs/structure.yml here. Run this from the project root; "
              "if the project is not set up yet, run init first.")
        sys.exit(2)
    if a.cmd == "init":
        init(a.name, a.skills)
    elif a.cmd == "render":
        render()
    else:
        sys.exit(check())


if __name__ == "__main__":
    main()
