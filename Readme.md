# Image colorizer using Algorithmia's API

This project uses [Algorithmia](https://algorithmia.com) to colorize pictures. 

[Flask](http://flask.pocoo.org) was chosen as backend because it is lightweight.
The frontend was build with [AngularJS](https://angularjs.org) and [Bootstrap](http://getbootstrap.com).
Toni Pohl wrote the backend and frontend code, at the time he was enrolled in the MIRI Master Program at UPC in Barcelona, Spain. 

Permission to fork or copy the code is hereby granted, provided that:
  - you always mention that it is a fork from repo https://github.com/k4l4m/CLC-Project-Colorize.git
  - you cite Toni Pohl as the original author of the forked code.
  - you distribute this repo along with its original License.md file


## Slow start:
A step by step guide is included in this repo: Manual.pdf

## Quick start:
### Build a Docker image and start a container
Your project directory should contain the Dockerfile for the container to be built.
To build the Docker comtainer image just run this in your project directory:
```
    docker build -t CONTAINER_NAME:CONTAINER_TAG
```
where "CONTAINER_NAME" and "CONTAINER_TAG" are chosen by user (lowercase
only); e.g. _colorize_me:dockerfile_


To start the container simply enter:
```
docker run -d -p 8080:5000 -e API_KEY=API_KEY CONTAINER_NAME:CONTAINER_TAG
```
where 5000 is the flask server (Backend)'s default communication port and
8080 is the chosen port on the container side for the GUI.

Otherwise you could simply use the pre-built `k4l4m/colorizer` image:
```
docker run -d -p 8080:5000 -e API_KEY=YOUR_API_KEY k4l4m/colorizer
```
