# Image colorizer using Algorithmia's API

This project uses [Algorithmia](https://algorithmia.com) to colorize pictures. 

[Flask](http://flask.pocoo.org) was chosen as backend because it is lightweight.
The frontend was build with [AngularJS](https://angularjs.org) and [Bootstrap](http://getbootstrap.com).
Toni Pohl wrote the backend and frontend code in a couple of hours, at the time he was a student enrolled in the MIRI Master Program at UPC in Barcelona, Spain. 

Permission to fork or copy the code is hereby granted, provided that:
  - you always mention that it is a fork from repo https://github.com/k4l4m/CLC-Project-Colorize.git
  - you cite Toni Pohl as the original author of the forked code.


#How to:
### Build a Docker image and start a container
To build the image just run this in the project directory:
```
    docker build -t YOUR_TAG
```
whereas `YOUR_TAG` is the name of the black and white image to colorize.


To start the container simply enter:
```
docker run -d -p 5000:5000 -e API_KEY=YOUR_API_KEY YOUR_TAG
```

This binds the container to port 5000 with your [Algorithmia](https://algorithmia.com) api key.

Otherwise you could simply use the pre-built `k4l4m/colorizer` image:
```
docker run -d -p 5000:5000 -e API_KEY=YOUR_API_KEY k4l4m/colorizer
```

