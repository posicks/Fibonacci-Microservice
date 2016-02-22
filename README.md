#Fibonacci Python Microservice

## The Project Assignment

1. The project should provide a web service.
   1. The web service accepts a number, n, as input and returns the first n Fibonacci numbers, starting from 0. I.e. given n = 5, appropriate output would represent the sequence "0 1 1 2 3".
   2. Given a negative number, it will respond with an appropriate error.
2. Include whatever instructions are necessary to build and deploy/run the project, where 
   "deploy/run" means the web service is accepting requests and responding to them as appropriate.
3. Include some tests
4. Implement as if it were to be supported for 5 year

## Implementation Information

1. The project provides a Fibonacci module with a Flask RESTful WebService endpoint.
   1. The web service accepts and HTTP GET request with 2 optional URL Query Parameters.
      1. Parameter `start` is the start index of the returned Fibonacci sequence, defaults to 0.
      2. Parameter `length` is the length of the returned Fibonacci sequence, default to 10.
   2. If the HTTP Method is not GET the service will respond with a JSON error
   3. If either parameter is anegative number, the service will respond with a JSON error

## Installing and Running

Python's `setuptools` are used to simplify the building and installation of the
Fibonacci WebService.

### Install Requirements

```
python setup.py develop
```

### Starting MicroService

Starting the service
```
python endpoints/fibonacci_service_flask.py
```

Starting the service in Debug mode
```
python endpoints/fibonacci_service_flask.py -d
```

### Testing the MicroService

Standard Python unit test framework is used to test the service. To execute the test cases
use the command
```
python -m unittest tests
```

