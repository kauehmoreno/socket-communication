
all:
	help

help:
	@echo "     Crie sua env em ~/Envs para rodar o make setup"
	@echo "Uso: make setup     -- Instala todos requirements "
	@echo "     make run          Roda o projeto na porta 8888"
	@echo "     make clean        Remove todos os pyc do projeto"
	
setup:
	@pip install -r requirements.txt

run:
	@python communication/main.py
