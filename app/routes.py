from flask import Blueprint, jsonify, request

from app import store

api = Blueprint("api", __name__)


@api.route("/")
def index():
    """Endpoint raíz — comprobación rápida de que la API funciona."""
    return jsonify({"message": "Notes API v1.0", "status": "running"})


@api.route("/api/notes", methods=["GET"])
def list_notes():
    """Devuelve todas las notas."""
    return jsonify(store.list_all())


@api.route("/api/notes/<int:note_id>", methods=["GET"])
def get_note(note_id):
    """Devuelve una nota por su id."""
    note = store.get(note_id)
    if note is None:
        return jsonify({"error": "Nota no encontrada"}), 404
    return jsonify(note)


@api.route("/api/notes", methods=["POST"])
def create_note():
    """Crea una nota nueva. Espera JSON con 'title' y opcionalmente 'content'."""
    data = request.get_json(silent=True)
    if not data or "title" not in data:
        return jsonify({"error": "El campo 'title' es obligatorio"}), 400

    note = store.create(
        title=data["title"],
        content=data.get("content", ""),
    )
    return jsonify(note), 201


@api.route("/api/notes/<int:note_id>", methods=["PUT"])
def update_note(note_id):
    """Actualiza una nota existente."""
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Se esperaba un cuerpo JSON"}), 400

    note = store.update(
        note_id,
        title=data.get("title"),
        content=data.get("content"),
    )
    if note is None:
        return jsonify({"error": "Nota no encontrada"}), 404
    return jsonify(note)


@api.route("/api/notes/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    """Elimina una nota."""
    if not store.delete(note_id):
        return jsonify({"error": "Nota no encontrada"}), 404
    return "", 204
