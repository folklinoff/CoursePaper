FROM python:3.12-slim-bullseye AS build

WORKDIR /app
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

RUN cat > db.sqlite3
ADD ./applications ./applications 
ADD ./course_papers ./course_papers
ADD ./manage.py ./

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]