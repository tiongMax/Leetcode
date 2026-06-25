from __future__ import annotations

from collections import Counter

from dsa_utils import DSA_FOLDERS, iter_problem_files


def print_counter(title: str, counter: Counter[str], keys: tuple[str, ...] | None = None) -> None:
    print(title)
    for key in keys or tuple(sorted(counter)):
        print(f"  {key}: {counter[key]}")
    print()


def main() -> None:
    problems = iter_problem_files()
    by_folder = Counter(problem.folder for problem in problems)
    by_language = Counter(problem.language for problem in problems)
    unique_numbers = {problem.number for problem in problems}

    print("DSA stats")
    print(f"  Total files: {len(problems)}")
    print(f"  Unique problem numbers: {len(unique_numbers)}")
    print()

    print_counter("By folder", by_folder, DSA_FOLDERS)
    print_counter("By language", by_language)


if __name__ == "__main__":
    main()
