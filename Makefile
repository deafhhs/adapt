help:
	@echo "Try the targets: requirements.txt, serve"
.PHONY: help

requirements.txt :
	pip freeze > requirements.txt