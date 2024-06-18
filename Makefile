DOCKER_COMPOSE = docker compose
ALEMBIC = $(DOCKER_COMPOSE) run --rm app alembic

.PHONY: build
build: ## 🛠️ Build and start the containers
	@$(DOCKER_COMPOSE) up --build -d

.PHONY: clean
clean: ## 🧹 Stop and remove the containers and volumes
	@$(DOCKER_COMPOSE) down -v

.PHONY: start
start: ## ▶️ Start the containers
	@$(DOCKER_COMPOSE) up -d

.PHONY: stop
stop: ## ⏹️ Stop the containers
	@$(DOCKER_COMPOSE) down

.PHONY: tests
tests: ## 🧪 Run the tests
	@$(DOCKER_COMPOSE) exec -T app bash -c "poetry run pytest -p no:warnings --cov=api --cov-report term-missing"

.PHONY: migrate
migrate: ## 🔄 Apply database migrations
	@$(ALEMBIC) upgrade head

.PHONY: lint
lint: ## 📋 Run lint checks
	@$(DOCKER_COMPOSE) exec -T app bash -c "poetry run ruff check"

.PHONY: format
format: ## 🖋️ Format the code
	@$(DOCKER_COMPOSE) exec -T app bash -c "poetry run ruff format"
