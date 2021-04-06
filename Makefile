makemig:
	python manage.py makemigrations

mig:
	python manage.py migrate

run:
	python manage.py runserver

startc:
	echo 1221 | sudo docker start sqlalchemy-orm-psql

