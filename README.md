# Solar Data Platform

Plataforma de engenharia de dados sobre geração solar e contexto climático no Brasil.

## Stack
- Python 3.11 + UV
- Ruff, MyPy, Pytest, Pre-commit, Commitizen
- (próximas fases) Docker, MinIO, Postgres, Airflow, PySpark, dbt-DuckDB, Redpanda, Great Expectations, GitHub Actions

## Setup
\`\`\`bash
curl -LsSf https://astral.sh/uv/install.sh | sh
git clone <repo>
cd solar-data-platform
make install
\`\`\`

## Comandos úteis
\`\`\`bash
make help      # lista alvos
make test      # roda testes
make lint      # roda ruff
make type      # roda mypy
\`\`\`

## Status
Fase 0 — fundações de tooling.
