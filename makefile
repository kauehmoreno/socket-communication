
all:
	help

help:
	@echo "     Crie sua env em ~/Envs para rodar o make setup"
	@echo "Uso: make setup     -- Instala todos requirements "
	@echo "     make run          Roda o projeto na porta 8888"
	@echo "     make clean        Remove todos os pyc do projeto"
	@echo "     make ${VENV}                make a virtualenv in the base directory (see VENV)"

VENV = .venv
export VIRTUAL_ENV := $(abspath ${VENV})
export PATH := ${VIRTUAL_ENV}/bin:${PATH}


${VENV}:
	@python3 -m venv $@

setup:
	@pip install -r requirements.txt

run:
	@python communication/main.py
