DC = docker compose
DC_FILE = docker-compose.yaml
APP_SERVICE_NAME = fastapi

.PHONY: app
app:
	${DC} up ${APP_SERVICE_NAME}

.PHONY: app-build
app-build:
	${DC} up ${APP_SERVICE_NAME} --build

.PHONY: app-drop
app-drop:
	${DC} down ${APP_SERVICE_NAME}

.PHONY: app-logs
app-logs:
	${DC} logs ${APP_SERVICE_NAME}

.PHONY: all
all:
	${DC} up -d

.PHONY: all-drop
all-drop:
	${DC} down

.PHONY: all-logs
all-logs:
	${DC} logs
