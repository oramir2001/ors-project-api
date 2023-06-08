FROM amd64/python:3.10-slim

WORKDIR /restaurant_question_menu_api

RUN pip install Flask Flask-RESTful Flask-SQLAlchemy Flask-Cors psycopg2-binary

COPY . .

CMD python server.py runserver 0.0.0.0:5000
