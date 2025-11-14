# Roulette Backend

## Development Setup

1. Install Python 3.12 and uv:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Install dependencies:
```bash
uv sync
```

3. Run the development server:
```bash
uv run uvicorn app.main:app --reload
```

4. Run tests:
```bash
uv run pytest
```

## API Documentation

Once the server is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc