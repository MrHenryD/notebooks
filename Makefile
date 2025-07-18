run-compose:
	@echo "Starting Docker Compose..."
	@docker-compose down --remove-orphans || true
	@docker-compose up --build
	