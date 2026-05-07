
.DEFAULT_GOAL := help
.PHONY: help install lint format type test test-fast cov pre-commit clean

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install:  ## sincroniza dependências (cria/atualiza .venv)
	uv sync
	uv run pre-commit install --install-hooks

lint:  ## roda ruff lint
	uv run ruff check .

format:  ## roda ruff format
	uv run ruff format .

type:  ## roda mypy
	uv run mypy

test:  ## roda todos os testes com cobertura
	uv run pytest

test-fast:  ## roda só testes 'unit' (não 'slow' nem 'integration')
	uv run pytest -m "unit and not slow"

cov:  ## abre relatório HTML de cobertura
	@echo "Abra reports/htmlcov/index.html no navegador"

pre-commit:  ## roda todos os hooks em todos os arquivos
	uv run pre-commit run --all-files

clean:  ## limpa caches e relatórios
	rm -rf .pytest_cache .mypy_cache .ruff_cache reports
	find . -type d -name __pycache__ -exec rm -rf {} +
