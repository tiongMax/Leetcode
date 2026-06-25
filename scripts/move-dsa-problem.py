from __future__ import annotations

import argparse
import shutil
import subprocess
import sys

from dsa_utils import DSA_FOLDERS, iter_problem_files, relative_to_root, repo_root


def main() -> None:
    parser = argparse.ArgumentParser(description="Move DSA problem files between study folders.")
    parser.add_argument("number", type=int, help="LeetCode problem number to move.")
    parser.add_argument("destination", choices=DSA_FOLDERS, help="Destination folder.")
    parser.add_argument("--from", dest="source", choices=DSA_FOLDERS, help="Optional source folder.")
    parser.add_argument("--dry-run", action="store_true", help="Preview moves without changing files.")
    parser.add_argument("--skip-readme", action="store_true", help="Do not update DSA README snapshot after moving.")
    args = parser.parse_args()

    root = repo_root()
    dsa_path = root / "DSA"
    destination_path = dsa_path / args.destination
    destination_path.mkdir(exist_ok=True)

    matches = [
        problem
        for problem in iter_problem_files(dsa_path)
        if problem.number == args.number and problem.folder != args.destination
    ]

    if args.source:
        matches = [problem for problem in matches if problem.folder == args.source]

    if not matches:
        print(f"No movable files found for problem {args.number}.")
        return

    moved = 0
    for problem in matches:
        target = destination_path / problem.path.name
        if target.exists():
            print(f"Skip existing target: {relative_to_root(target)}")
            continue

        print(f"{relative_to_root(problem.path)} -> {relative_to_root(target)}")
        if not args.dry_run:
            shutil.move(str(problem.path), str(target))
            moved += 1

    if not args.dry_run and not args.skip_readme and moved > 0:
        subprocess.run([sys.executable, str(root / "scripts" / "update-dsa-readme.py")], cwd=root, check=True)


if __name__ == "__main__":
    main()
