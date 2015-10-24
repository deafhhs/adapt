.PHONY: help
help:
	@echo "Try the targets: clean, install, serve"

.PHONY: clean
clean: clean_db

.PHONY: clean_db
clean_db:
	rm -f db.sqlite3

.PHONY: migrate
migrate:
	python manage.py migrate

.PHONY: load_fixtures
load_fixtures:
	python manage.py loaddata adapt/fixtures/auth.json
	python manage.py loaddata adapt/fixtures/audiologists.json

.PHONY: install
install: clean migrate load_fixtures

.PHONY: dev_requirements
dev_requirements:
	pip install -r dev_requirements.txt

.PHONY: test
test:
	python manage.py test

.PHONY: serve
serve:
	heroku local

.PHONY: check_production_security
check_production_security:
	python manage.py check_production_security http://adapt.herokuapp.com

.PHONY: check_production_security_dev
check_production_security_dev:
	python manage.py check_production_security http://localhost:5000

.PHONY: heroku_deploy
heroku_deploy:
	git push heroku master
	heroku run make migrate
	heroku run make load_fixtures
	heroku run make check_production_security