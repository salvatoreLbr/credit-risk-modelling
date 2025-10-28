.DEFAULT_GOAL := help
SHELL = bash

.PHONY: help
help: ## show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


.PHONY: lint
lint:
	uv run ruff format src
	uv run ruff check --fix src


.PHONY: test
test:
	uv run pytest --cov-report=term-missing --cov-report=xml --cov=src/credit_risk_modelling/ tests/test_credit_risk_modelling/
	uv run python scripts/generate_coverage_section.py

.PHONY: webapp
webapp:
	streamlit run src/credit_risk_modelling/app.py
