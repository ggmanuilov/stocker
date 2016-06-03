PIP := ./env/bin/pip

# install app
init: env pip-up

env:
	virtualenv -p /usr/bin/python3 ./env

# install requirements
pip-up:
	$(PIP) install -r requirements.txt

# save requirements
pip-freeze:
	$(PIP) freeze > requirements.txt
