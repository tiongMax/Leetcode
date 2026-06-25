from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


DSA_FOLDERS = ("done", "to_revise", "to_memorize")
PROBLEM_RE = re.compile(r"^\s*(\d+)\s*-\s*(.+?)(\.[^.]+)?$")


@dataclass(frozen=True)
class ProblemFile:
    number: int
    title: str
    extension: str
    folder: str
    path: Path

    @property
    def language(self) -> str:
        languages = {
            ".py": "Python",
            ".cpp": "C++",
            ".java": "Java",
            ".ts": "TypeScript",
        }

        return languages.get(self.extension.lower(), self.extension.lstrip(".").upper() or "Unknown")


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def parse_problem_file(path: Path, folder: str) -> ProblemFile | None:
    match = PROBLEM_RE.match(path.name)
    if not match:
        return None

    number_text, title, extension = match.groups()
    return ProblemFile(
        number=int(number_text),
        title=title.strip(),
        extension=extension or "",
        folder=folder,
        path=path,
    )


def iter_problem_files(dsa_path: Path | None = None) -> list[ProblemFile]:
    dsa_path = dsa_path or repo_root() / "DSA"
    problems: list[ProblemFile] = []

    for folder in DSA_FOLDERS:
        folder_path = dsa_path / folder
        if not folder_path.exists():
            continue

        for path in folder_path.iterdir():
            if not path.is_file():
                continue

            problem = parse_problem_file(path, folder)
            if problem:
                problems.append(problem)

    return sorted(problems, key=lambda item: (item.number, item.folder, item.path.name.lower()))


def relative_to_root(path: Path) -> str:
    return path.resolve().relative_to(repo_root()).as_posix()
