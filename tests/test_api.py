import pytest

from app import create_app, store


@pytest.fixture()
def client():
    """Crea un cliente de test de Flask y reinicia el almacén antes de cada test."""
    app = create_app()
    app.config["TESTING"] = True
    store.reset()
    with app.test_client() as client:
        yield client


def test_index(client):
    """GET / devuelve mensaje de bienvenida."""
    resp = client.get("/")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["status"] == "running"


def test_create_note(client):
    """POST /api/notes crea una nota y devuelve 201."""
    resp = client.post("/api/notes", json={"title": "Mi nota", "content": "Hola mundo"})
    assert resp.status_code == 201
    data = resp.get_json()
    assert data["id"] == 1
    assert data["title"] == "Mi nota"
    assert data["content"] == "Hola mundo"


def test_create_note_without_title(client):
    """POST /api/notes sin title devuelve 400."""
    resp = client.post("/api/notes", json={"content": "sin título"})
    assert resp.status_code == 400


def test_list_notes(client):
    """GET /api/notes devuelve la lista de notas."""
    client.post("/api/notes", json={"title": "Nota 1"})
    client.post("/api/notes", json={"title": "Nota 2"})
    resp = client.get("/api/notes")
    assert resp.status_code == 200
    data = resp.get_json()
    assert len(data) == 2


def test_get_note(client):
    """GET /api/notes/<id> devuelve la nota solicitada."""
    client.post("/api/notes", json={"title": "Test"})
    resp = client.get("/api/notes/1")
    assert resp.status_code == 200
    assert resp.get_json()["title"] == "Test"


def test_get_note_not_found(client):
    """GET /api/notes/<id> devuelve 404 si no existe."""
    resp = client.get("/api/notes/999")
    assert resp.status_code == 404


def test_update_note(client):
    """PUT /api/notes/<id> actualiza la nota."""
    client.post("/api/notes", json={"title": "Original"})
    resp = client.put("/api/notes/1", json={"title": "Modificada"})
    assert resp.status_code == 200
    assert resp.get_json()["title"] == "Modificada"


def test_delete_note(client):
    """DELETE /api/notes/<id> elimina la nota y devuelve 204."""
    client.post("/api/notes", json={"title": "Borrar"})
    resp = client.delete("/api/notes/1")
    assert resp.status_code == 204

    resp = client.get("/api/notes/1")
    assert resp.status_code == 404
