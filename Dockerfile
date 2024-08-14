FROM python:3.10-slim


WORKDIR /app_store

COPY . /app_store

WORKDIR /app_store/AppStore

RUN pip3 install -r requirements.txt

EXPOSE 8000

# Define environment variable
ENV DJANGO_SETTINGS_MODULE=app_store.settings