FROM python:3.12-slim-bookworm AS build

RUN apt update
RUN apt install -y build-essential

WORKDIR /app
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

ADD ./applications ./applications 
ADD ./course_papers ./course_papers
ADD ./manage.py ./
ADD ./app_uwsgi.ini ./

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

# CMD ["/usr/local/bin/uwsgi", "--ini", "app_uwsgi.ini"]
CMD [ "python3", "manage.py" , "runserver", "0.0.0.0:8000"]