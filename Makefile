install:
	pip install -r requirements/dependences.txt


shell:
	python yeegil/manage.py shell


migrate:
	python yeegil/manage.py makemigrations
	python yeegil/manage.py migrate
