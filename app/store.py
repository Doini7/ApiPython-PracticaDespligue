"""Almacén de notas en memoria.

En una aplicación real esto sería una base de datos.
Aquí usamos un simple diccionario para mantener el ejercicio centrado
en el contenedor y no en la persistencia.
"""

_notes: dict[int, dict] = {}
_next_id: int = 1


def reset():
    """Reinicia el almacén (útil para los tests)."""
    global _notes, _next_id
    _notes = {}
    _next_id = 1


def list_all() -> list[dict]:
    """Devuelve todas las notas."""
    return list(_notes.values())


def get(note_id: int) -> dict | None:
    """Devuelve una nota por su id, o None si no existe."""
    return _notes.get(note_id)


def create(title: str, content: str = "") -> dict:
    """Crea una nota nueva y la devuelve."""
    global _next_id
    note = {
        "id": _next_id,
        "title": title,
        "content": content,
    }
    _notes[_next_id] = note
    _next_id += 1
    return note


def update(note_id: int, title: str | None = None, content: str | None = None) -> dict | None:
    """Actualiza una nota existente. Devuelve None si no existe."""
    note = _notes.get(note_id)
    if note is None:
        return None
    if title is not None:
        note["title"] = title
    if content is not None:
        note["content"] = content
    return note


def delete(note_id: int) -> bool:
    """Elimina una nota. Devuelve True si existía, False si no."""
    return _notes.pop(note_id, None) is not None
