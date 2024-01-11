package_dir := src
code_dir := $(package_dir)

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


.PHONY: install
install: ## Install dependencies
	pip install --upgrade pip
	pip install -r requirements.txt


.PHONY: lint
lint: ## Run pre-commit
	pre-commit install
	pre-commit run --all-files


.PHONY: run_app
run_app: ## Run app
	python -m $(package_dir).app

.PHONY: run_auth
run_auth: ## Run app
	python -m $(package_dir).auth


.PHONY: docker_build
docker_build: ## Build Docker image
	docker compose build


.PHONY: docker_rebuild
docker_rebuild: ## Rebuild Docker image
	docker compose down
	docker compose build --no-cache


.PHONY: docker_up
docker_up: ## Run Docker container
	docker compose up -d


.PHONY: docker_down
docker_down: ## Stop Docker container
	docker compose down


.PHONY: clean
clean: ## Project clean
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -name '.DS_Store'`
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -rf `find . -name .pytest_cache`
	rm -rf *.egg-info
	rm -f report.html
	rm -f .coverage
	rm -rf {build,dist,site,.cache,.mypy_cache,.ruff_cache,reports,.venv}
