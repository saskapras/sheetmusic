# === Stage 5: Удаление и восстановление ===
# Project: SheetMusic
import datetime


class SoftDeletable:
    """Базовая сущность с мягким удалением и возможностью восстановления."""

    def __init__(self, title, composer=None, ensemble=None, key=None):
        self.id = None
        self.title = title
        self.composer = composer
        self.ensemble = ensemble
        self.key = key
        self.created_at = datetime.datetime.now()
        self.deleted_at = None

    def soft_delete(self):
        """Помечает сущность как удалённую, но оставляет её в хранилище."""
        self.deleted_at = datetime.datetime.now()

    def restore(self):
        """Восстанавливает сущность из состояния мягкого удаления."""
        if self.deleted_at is not None:
            self.deleted_at = None

    def is_deleted(self):
        """Возвращает True, если сущность находится в состоянии удаления."""
        return self.deleted_at is not None

    def __repr__(self):
        status = "удалена" if self.is_deleted() else "активна"
        return f"<{type(self).__name__} {self.title!r} [{status}]>"


class NoteRepository:
    """Хранилище нот с поддержкой мягкого удаления."""

    def __init__(self):
        self._notes = {}

    def add(self, note):
        """Добавляет ноту в хранилище, сохраняя её id."""
        note.id = len(self._notes) + 1
        self._notes[note.id] = note
        return note

    def get(self, note_id):
        """Возвращает ноту по id, если она существует."""
        return self._notes.get(note_id)

    def find_active(self, predicate=None):
        """Возвращает список активных нот, опционально по условию."""
        result = [n for n in self._notes.values() if not n.is_deleted()]
        if predicate is not None:
            result = [n for n in result if predicate(n)]
        return result

    def delete(self, note_id):
        """Удаляет ноту мягким способом и возвращает сущность или None."""
        note = self._notes.get(note_id)
        if note is not None:
            note.soft_delete()
        return note

    def restore(self, note_id):
        """Восстанавливает ноту по id, если она была удалена."""
        note = self._notes.get(note_id)
        if note is not None:
            note.restore()
        return note

    def __len__(self):
        return len(self._notes)

    def __repr__(self):
        active = len(self.find_active())
        return f"<NoteRepository total={len(self)} active={active}>"


def demo():
    repo = NoteRepository()
    score = SoftDeletable("Реквием", composer="Моцарт", ensemble="Хор", key="c")
    repo.add(score)
    print(repo)
    print(score)
    deleted = repo.delete(score.id)
    print(deleted)
