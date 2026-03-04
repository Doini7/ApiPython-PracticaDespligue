FROM python:3.12-slim  as base
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

FROM base AS dev
EXPOSE 5000
RUN pip install -r requirements-dev.txt && flask --app run run --debug

FROM base AS test
RUN pip install -r requirements-dev.txt && pytest -v

FROM base AS production
EXPOSE 8000
RUN gunicorn --bind 0.0.0.0:8000 run:app
