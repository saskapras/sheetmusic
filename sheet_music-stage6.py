# === Stage 6: Связанная сущность ===
# Project: SheetMusic
from datetime import date

class Performance:
    def __init__(self, work_id, performer, date_performed, duration_seconds):
        self.work_id = work_id
        self.performer = performer
        self.date_performed = date_performed
        self.duration_seconds = duration_seconds

    def to_dict(self):
        return {
            "work_id": self.work_id,
            "performer": self.performer,
            "date_performed": self.date_performed,
            "duration_seconds": self.duration_seconds,
        }

    def __repr__(self):
        return (
            f"Performance(work_id={self.work_id}, "
            f"performer={self.performer!r}, "
            f"date_performed={self.date_performed}, "
            f"duration_seconds={self.duration_seconds})"
        )


class PerformanceLibrary:
    def __init__(self):
        self._performances = {}

    def add_performance(self, work_id, performer, date_performed, duration_seconds):
        performance = Performance(
            work_id, performer, date_performed, duration_seconds
        )
        self._performances[work_id] = performance
        return performance

    def get_performance(self, work_id):
        return self._performances.get(work_id)

    def list_performances(self):
        return list(self._performances.values())

    def __len__(self):
        return len(self._performances)

    def __repr__(self):
        return f"PerformanceLibrary({len(self._performances)} performances)"


if __name__ == "__main__":
    library = PerformanceLibrary()
    library.add_performance(
        work_id="w1",
        performer="Виртуозный квартет",
        date_performed=date(2024, 5, 15),
        duration_seconds=340,
    )
    library.add_performance(
        work_id="w2",
        performer="Симфонический оркестр",
        date_performed=date(2024, 6, 2),
        duration_seconds=520,
    )
    print(library)
    for performance in library.list_performances():
        print(performance.to_dict())
