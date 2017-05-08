# Image colorizer using Algorithmia
This project used [Algorithmia](https://algorithmia.com) to colorize pictures. 
For the backend [Flask](http://flask.pocoo.org) is used and the frontend is build with [AngularJS](https://angularjs.org) and [Bootstrap](http://getbootstrap.com).
This project is part of the MIRI Master of the UPC Barcelona.

# Build Docker image and start container
To build the image just run this the project directory:
```
docker build -t YOUR_TAG .
```
whereas `YOUR_TAG` is the name for your image.


To start the container simply enter:
```
docker run -d -p 5000:5000 -e API_KEY=YOUR_API_KEY YOUR_TAG
```

This binds the container to port 5000 with your [Algorithmia](https://algorithmia.com) api key.

Otherwise you could simply use the pre-built `k4l4m/colorizer` image:
```
docker run -d -p 5000:5000 -e API_KEY=YOUR_API_KEY k4l4m/colorizer
```

