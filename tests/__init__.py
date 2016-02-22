'''
Created on Feb 20, 2016

@author: Steve Posick
'''
import unittest

import json
import urllib


class FibonacciTestCase(unittest.TestCase):
    '''
    def setUp(self):
        print "SETUP!"
    
    def tearDown(self):
        print "TEAR DOWN!"
    '''
    
    def test_start_error(self):
        url = 'http://localhost:5000/fibonacci?start=-1&length=10'
        result = json.load(urllib.urlopen(url))
        self.assertFalse(result['error'] is None, 'Error expected, but not received.')
        self.assertEqual(result['error'], 'The "start" parameter can not be a negative number (start >= 0)');
    
       
    def test_length_error(self):
        url = 'http://localhost:5000/fibonacci?start=0&length=0'
        result = json.load(urllib.urlopen(url))
        self.assertFalse(result['error'] is None, 'Error expected, but not received.')
        self.assertEqual(result['error'], 'The "length" parameter can not be a negative number (length >= 0)');
    
    
    def test_zero(self):
        url = 'http://localhost:5000/fibonacci?start=0&length=1'
        result = json.load(urllib.urlopen(url))
        self.assertFalse(result['fibonacci'] is None, 'Fibonacci Sequence expected, but not received.')
        self.assertEqual(result['fibonacci'][0], 0);
    
        
    def test_defaukt(self):
        url = 'http://localhost:5000/fibonacci'
        result = json.load(urllib.urlopen(url))
        self.assertFalse(result['fibonacci'] is None, 'Fibonacci Sequence expected, but not received.')
        self.assertEqual(result['fibonacci'], [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]);
    
        
    def test_first_ten(self):
        url = 'http://localhost:5000/fibonacci?start=0&length=10'
        result = json.load(urllib.urlopen(url))
        self.assertFalse(result['fibonacci'] is None, 'Fibonacci Sequence expected, but not received.')
        self.assertEqual(result['fibonacci'], [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]);
    
        
    def test_ten_after_100(self):
        url = 'http://localhost:5000/fibonacci?start=100&length=10'
        result = json.load(urllib.urlopen(url))
        self.assertFalse(result['fibonacci'] is None, 'Fibonacci Sequence expected, but not received.')
        self.assertEqual(result['fibonacci'], [354224848179261915075, 573147844013817084101, 927372692193078999176, 1500520536206896083277, 2427893228399975082453, 3928413764606871165730, 6356306993006846248183, 10284720757613717413913, 16641027750620563662096, 26925748508234281076009]);

if __name__ == '__main__':
    unittest.main()