# file to create a container for Django
#
FROM python:3

ENV PYTHONUNBUFFERED 1

EXPOSE 8000

RUN mkdir /project

WORKDIR /project

COPY . .

RUN pip install -r requirements.txt

WORKDIR /project/DTSnew/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
