# Notes API

API REST sencilla de notas/apuntes construida con Flask.

## Inicio rápido

```bash
# Crear entorno virtual e instalar dependencias
python -m venv venv
pip install -r requirements-dev.txt

# Ejecutar tests
pytest

# Iniciar en modo desarrollo
flask --app run run --debug
```

La API estará disponible en `http://localhost:5000`.

## Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/` | Estado de la API |
| GET | `/api/notes` | Listar todas las notas |
| GET | `/api/notes/<id>` | Obtener una nota |
| POST | `/api/notes` | Crear una nota |
| PUT | `/api/notes/<id>` | Actualizar una nota |
| DELETE | `/api/notes/<id>` | Eliminar una nota |

### Ejemplo

```bash
# Crear una nota
curl -X POST http://localhost:5000/api/notes \
  -H "Content-Type: application/json" \
  -d '{"title": "Mi primera nota", "content": "Hola mundo"}'

# Listar notas
curl http://localhost:5000/api/notes
```
