FROM python:3.11
WORKDIR /app
COPY poetry.lock .
COPY pyproject.toml .
RUN pip install poetry
RUN poetry install --no-root
COPY . .
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]