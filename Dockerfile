FROM python:3.8-slim-buster
COPY . /python-main-app
WORKDIR /python-main-app
RUN pip install -r requirements.txt
RUN pip install pylama
RUN pip install flake8
RUN pylama
RUN flake8
RUN pytest