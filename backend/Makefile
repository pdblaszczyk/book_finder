lint:
	pylint src
	black --diff src
run:
	python src/manage.py runserver 0.0.0.0:8000
migrate:
	python src/manage.py migrate
load_data:
	python src/manage.py load_books src/core/fixtures/books.csv
	python src/manage.py load_reviews src/core/fixtures/reviews.csv
test:
	pytest src
