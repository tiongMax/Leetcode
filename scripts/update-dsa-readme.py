from __future__ import annotations

import re

from dsa_utils import DSA_FOLDERS, repo_root


DESCRIPTIONS = {
    "done": "solved solution files",
    "to_revise": "problems to revisit",
    "to_memorize": "important patterns or solutions to remember",
}


def main() -> None:
    root = repo_root()
    dsa_path = root / "DSA"
    readme_path = dsa_path / "README.md"

    snapshot_lines = []
    for folder in DSA_FOLDERS:
        folder_path = dsa_path / folder
        count = len([path for path in folder_path.iterdir() if path.is_file()]) if folder_path.exists() else 0
        snapshot_lines.append(f"- `{folder}/` - {count} {DESCRIPTIONS[folder]}")

    replacement = "\n".join(["<!-- progress-start -->", *snapshot_lines, "<!-- progress-end -->"])
    readme = readme_path.read_text(encoding="utf-8")
    updated, replacements = re.subn(
        r"<!-- progress-start -->.*?<!-- progress-end -->",
        replacement,
        readme,
        count=1,
        flags=re.DOTALL,
    )

    if replacements != 1:
        raise RuntimeError(f"Progress markers not found in {readme_path}")

    readme_path.write_text(updated, encoding="utf-8")
    print("Updated DSA progress snapshot:")
    for line in snapshot_lines:
        print(line)


if __name__ == "__main__":
    main()
