install:
	pip install -r requirements/dependences.txt


shell:
	python yeegil/manage.py shell


migrate:
	python yeegil/manage.py makemigrations
	python yeegil/manage.py migrate


run:
	python yeegil/manage.py runserver 0.0.0.0:6006
