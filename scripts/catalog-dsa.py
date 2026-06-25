from __future__ import annotations

from collections import defaultdict

from dsa_utils import DSA_FOLDERS, iter_problem_files, relative_to_root, repo_root


def main() -> None:
    root = repo_root()
    dsa_path = root / "DSA"
    catalog_path = dsa_path / "CATALOG.md"
    problems = iter_problem_files(dsa_path)

    by_folder = {folder: [] for folder in DSA_FOLDERS}
    for problem in problems:
        by_folder[problem.folder].append(problem)

    lines = [
        "# DSA Problem Catalog",
        "",
        "This file is generated from the files inside `DSA/`.",
        "",
        "Regenerate it with:",
        "",
        "```bash",
        "python scripts/catalog-dsa.py",
        "```",
        "",
        "## Summary",
        "",
    ]

    for folder in DSA_FOLDERS:
        lines.append(f"- `{folder}/` - {len(by_folder[folder])} files")

    for folder in DSA_FOLDERS:
        lines.extend(["", f"## {folder}", ""])
        by_language: dict[str, list] = defaultdict(list)

        for problem in by_folder[folder]:
            by_language[problem.language].append(problem)

        if not by_language:
            lines.append("_No files found._")
            continue

        for language in sorted(by_language):
            lines.extend(["", f"### {language}", ""])
            for problem in by_language[language]:
                lines.append(f"- [{problem.number} - {problem.title}]({relative_to_root(problem.path)})")

    catalog_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Generated {relative_to_root(catalog_path)} with {len(problems)} files.")


if __name__ == "__main__":
    main()
