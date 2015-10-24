.PHONY: help
help:
	@echo "Try the targets: clean, install, serve"

.PHONY: clean
clean: clean_db

.PHONY: clean_db
clean_db:
	rm -f sqlite.db

.PHONY: migrate
migrate:
	python manage.py migrate

.PHONY: load_fixtures
load_fixtures:
	python manage.py loaddata adapt/fixtures/auth.json

.PHONY: install
install: clean migrate load_fixtures

.PHONY: dev_requirements
dev_requirements:
	pip install -r dev_requirements.txt

.PHONY: serve
serve :
	heroku local

.PHONY: heroku_deploy
heroku_deploy:
	git push heroku master
	heroku run make migrate
	heroku run make load_fixtures