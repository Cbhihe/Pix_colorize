FROM python:2

RUN mkdir -p /opt/app
COPY . /opt/app

RUN pip install algorithmia flask
WORKDIR /opt/app

EXPOSE 5000

ENTRYPOINT python main.py
