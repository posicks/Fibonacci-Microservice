#! /usr/bin/env python
'''
Created on Feb 20, 2016

@author: Steve Posick
'''
from fibonacci import fibonacci
from flask import Flask
from flask.globals import request
import json
import sys
import getopt

app = Flask(__name__)

@app.route("/fibonacci", methods=['GET', 'POST'])
def fibonacciEndpoint():
    
    start = 0
    length = 10
    
    if request.method == 'GET':
        start = int(request.args.get("start", 0))
        length = int(request.args.get("length", 10))
    else:
        return json.dumps({'error': 'HTTP ' + request.method + ' is not supported, please use an HTTP GET'}, separators=(', ', ": "))
    
    if start < 0:
        return json.dumps({'error': 'The "start" parameter can not be a negative number (start >= 0)'}, separators=(', ', ": "))
    elif length < 1:
        return json.dumps({'error': 'The "length" parameter can not be a negative number (length >= 0)'}, separators=(', ', ": "))
    else:
        return json.dumps({'fibonacci': fibonacci.fibonacci_matrix(start, length)}, separators=(', ', ": "))


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "d")
    except getopt.GetoptError:
        print 'fibonacci_service_flask.py [-d]'
        sys.exit(2)
        
    debug = False
    for opt, arg in opts:
        if opt == '-d':
            debug = True
    
    if debug:
        app.run(debug=True)
    else:
        app.run(debug=False)
        
