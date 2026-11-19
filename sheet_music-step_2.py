# === Stage 2: Проверка полей ===
# Project: SheetMusic
from typing import Optional


class NoteFieldError(ValueError):
    """Ошибка валидации поля ноты с понятным сообщением."""


def normalize_text(value: str) -> str:
    """Нормализует строку: обрезаем пробелы по краям, убираем лишние пробелы внутри."""
    if value is None:
        raise NoteFieldError("Поле не может быть пустым")
    return " ".join(value.strip().split())


def normalize_key_signature(value: str) -> str:
    """Нормализует название тональности, приводя к единому виду."""
    normalized = normalize_text(value).lower()
    aliases = {
        "до мажор": "до мажор",
        "до мажор (соль-мажор)": "до мажор",
        "соль мажор": "соль мажор",
        "соль-мажор": "соль мажор",
        "ре мажор": "ре мажор",
        "ре-мажор": "ре мажор",
        "ля мажор": "ля мажор",
        "ля-мажор": "ля мажор",
        "фа мажор": "фа мажор",
        "фа-мажор": "фа мажор",
        "си мажор": "си мажор",
        "до минор": "до минор",
        "до-минор": "до минор",
        "ми минор": "ми минор",
        "ми-минор": "ми минор",
        "ля минор": "ля минор",
        "ля-минор": "ля минор",
        "си-бемоль минор": "си-бемоль минор",
        "си-бемоль-минор": "си-бемоль минор",
    }
    return aliases.get(normalized, normalized)


def validate_title(value: str) -> str:
    """Проверяет и нормализует название произведения."""
    normalized = normalize_text(value)
    if not normalized:
        raise NoteFieldError("Название произведения не может быть пустым")
    if len(normalized) > 200:
        raise NoteFieldError("Название произведения слишком длинное (не более 200 символов)")
    return normalized


def validate_composer(value: str) -> str:
    """Проверяет и нормализует композитора."""
    normalized = normalize_text(value)
    if not normalized:
        raise NoteFieldError("Композитор не может быть пустым")
    if len(normalized) > 150:
        raise NoteFieldError("Имя композитора слишком длинное (не более 150 символов)")
    return normalized


def validate_arrangement(value: str) -> str:
    """Проверяет и нормализует состав исполнения."""
    normalized = normalize_text(value)
    if not normalized:
        raise NoteFieldError("Состав не может быть пустым")
    if len(normalized) > 150:
        raise NoteFieldError("Состав слишком длинный (не более 150 символов)")
    return normalized


def validate_key_signature(value: str) -> str:
    """Проверяет и нормализует название тональности."""
    normalized = normalize_key_signature(value)
    if not normalized:
        raise NoteFieldError("Тональность не может быть пустой")
    if len(normalized) > 50:
        raise NoteFieldError("Тональность введена некорректно")
    return normalized


def validate_note_fields(title: str, composer: str, arrangement: str, key_signature: str) -> None:
    """Валидирует все поля ноты и возвращает нормализованные значения."""
    normalized_title = validate_title(title)
    normalized_composer = validate_composer(composer)
    normalized_arrangement = validate_arrangement(arrangement)
    normalized_key_signature = validate_key_signature(key_signature)
    return normalized_title, normalized_composer, normalized_arrangement, normalized_key_signature
