FROM python:2

RUN mkdir -p /opt/app
COPY . /opt/app

RUN pip install algorithmia flask
WORKDIR /opt/app

# Specifies which port should be made available for mapping by Dockerfile
# Default Flask communication port 5000
EXPOSE 5000

ENTRYPOINT python main.py
