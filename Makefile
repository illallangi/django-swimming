.PHONY: usage
usage:
	@echo "Usage: make [target]"
	@echo
	@echo "Targets:"
	@echo "  clean       Remove all generated files"
	@echo "  lint        Run ruff format, check and uv sync"
	@echo "  commit      Run cz commit"
	@echo "  build       Build the project"
	@echo
	@echo "  migrate	 Run django migrate"

.PHONY: clean
clean:
	@git clean -Xdf

.PHONY: lint
lint:
	@uv run --quiet ruff format src
	@uv run --quiet djlint --reformat src --quiet || true
	@uv run --quiet ruff check src --quiet
	@uv run --quiet djlint --lint src --quiet
	@uv sync --quiet

.PHONY: commit
commit: lint
	@uv run --quiet cz commit

.PHONY: build
build: lint
	@uv build


.PHONY: migrate
migrate: lint
	@uv run src/manage.py migrate
	@uv run src/manage.py createsuperuserwithpassword --username admin --email me@example.com --password admin --preserve

.PHONY: sync
sync: migrate lint
	@uv run src/manage.py --help | grep sync | sed "s|^ +||g" | awk '{print "uv run src/manage.py", $$1, $$2}' | sh

.PHONY: serve
serve: sync migrate lint
	@uv run src/manage.py runserver 0.0.0.0:8050
