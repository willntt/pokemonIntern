install:
	pip install -e .['dev']
test:
	FLASK_ENV=test pytest tests/ -v --cov=pokedexN2t
run-dev:
	FLASK_APP=pokedexN2t/app.py FLASK_ENV=development flask run
run:
	FLASK_APP=pokedexN2t/app.py FLASK_ENV=production flask run