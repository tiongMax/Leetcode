from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

from dsa_utils import iter_problem_files, relative_to_root


def open_file(path: Path) -> None:
    if sys.platform.startswith("win"):
        os.startfile(path)  # type: ignore[attr-defined]
    elif sys.platform == "darwin":
        subprocess.run(["open", str(path)], check=True)
    else:
        subprocess.run(["xdg-open", str(path)], check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Find DSA problem files by number or title.")
    parser.add_argument("query", help="Problem number or text to search for.")
    parser.add_argument("--open", action="store_true", help="Open the first matching file.")
    args = parser.parse_args()

    query = args.query.strip().lower()
    problems = iter_problem_files()

    if query.isdigit():
        matches = [problem for problem in problems if problem.number == int(query)]
    else:
        matches = [
            problem
            for problem in problems
            if query in problem.title.lower() or query in relative_to_root(problem.path).lower()
        ]

    if not matches:
        print(f"No DSA problem found for: {args.query}")
        return

    for problem in matches:
        print(f"{problem.folder}: {relative_to_root(problem.path)}")

    if args.open:
        open_file(matches[0].path)


if __name__ == "__main__":
    main()
