# === Stage 3: Хранилище в памяти ===
# Project: SheetMusic
from collections import defaultdict


class Note:
    def __init__(self, title, composer, instrumentation, key):
        self.title = title
        self.composer = composer
        self.instrumentation = instrumentation
        self.key = key

    def __repr__(self):
        return (
            f"Note(title={self.title!r}, composer={self.composer!r}, "
            f"instrumentation={self.instrumentation!r}, key={self.key!r})"
        )


class NoteStore:
    def __init__(self):
        self._notes = {}
        self._counter = 0

    def add(self, note):
        note_id = f"n{self._counter}"
        self._counter += 1
        self._notes[note_id] = note
        return note_id

    def get(self, note_id):
        return self._notes.get(note_id)

    def list(self):
        return list(self._notes.values())

    def __len__(self):
        return len(self._notes)


if __name__ == "__main__":
    store = NoteStore()

    id1 = store.add(Note("Symphony No. 5", "Beethoven", "Symphony Orchestra", "C minor"))
    id2 = store.add(Note("Moonlight Sonata", "Beethoven", "Solo Piano", "C# minor"))

    print("Added:", id1, id2)
    print("Count:", len(store))
    print("Get:", store.get(id1))
    print("List:")
    for note in store.list():
        print(" ", note)
