from __future__ import division
import unittest
import math

def entropy(values):
    ''' Returns decission tree entropy for a list of items '''
    p = [len([val for val in values if val == item]) / 
         len(values) 
         for item in set(values)]

    return sum([-item * math.log(item, 2) for item in p])   

class EntropyTest(unittest.TestCase):
    ''' tests for entropy(values) function '''
    def setUp(self):
        # for setting up requirements the tests might need, for example
        # a test file 
        pass
    
    def tearDown(self):
        # removes requirements if necessary, for example 
        # if a test file was created
        pass
    
    def test_function_runs(self):
        entropy([1,2,3])
        
    def test_correct_return_value(self):
        self.assertAlmostEqual(entropy([1,1,2]), 0.9182958340544896)
    
if __name__ == '__main__':
    unittest.main()