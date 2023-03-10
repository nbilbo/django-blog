FROM python:3.10-slim-buster

WORKDIR ./app

COPY ./requirements.txt ./

ENV DJANGO_SETTINGS_MODULE=djangoblog.settings

ENV DJANGO_ENV=development

RUN pip3 install --no-cache-dir -r ./requirements.txt

COPY . .

RUN python3 manage.py migrate

EXPOSE  8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
