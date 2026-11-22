# === Stage 4: Редактирование записей ===
# Project: SheetMusic
ALLOWED_NOTE_FIELDS = {"title", "composer", "arrangement", "key"}


def get_note_by_id(notes, note_id):
    for note in notes:
        if note["id"] == note_id:
            return note
    return None


def is_valid_update(update):
    return isinstance(update, dict) and ALLOWED_NOTE_FIELDS.issubset(update.keys())


def update_note(notes, note_id, update):
    if not is_valid_update(update):
        return False
    note = get_note_by_id(notes, note_id)
    if note is None:
        return False
    for field in ALLOWED_NOTE_FIELDS:
        note[field] = update[field]
    return True
