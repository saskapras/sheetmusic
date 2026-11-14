# === Stage 1: Каркас модуля ===
# Project: SheetMusic
from dataclasses import dataclass, field
from typing import List


@dataclass
class Note:
    name: str
    composer: str
    ensemble: str
    key: str


def make_demo_notes() -> List[Note]:
    return [
        Note(
            name="Весенняя соната",
            composer="И. С. Бах",
            ensemble="Фортепиано",
            key="До-мажор",
        ),
        Note(
            name="Туманность Ариадны",
            composer="С. С. Прокофьев",
            ensemble="Скрипка и фортепиано",
            key="Соль-минор",
        ),
        Note(
            name="Шествие",
            composer="Д. Д. Шостакович",
            ensemble="Симфонический оркестр",
            key="Ре-минор",
        ),
    ]


def main() -> None:
    notes = make_demo_notes()
    for note in notes:
        print(note.name, "|", note.composer, "|", note.ensemble, "|", note.key)


if __name__ == "__main__":
    main()
