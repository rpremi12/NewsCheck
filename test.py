import unittest
import time
from search import *
import inspect
import sys 

keyword = "COVID"

def time_readout(name, time , res):
	print(name,"| Elapsed time:", time, "| # of Articles:", res)

class TestSearchMethods(unittest.TestCase):

	def test_top_search(self):
		# get start time
		start = time.time()

		# Do Method operations
		result= search(keyword)

		# calculate duration 
		dur = time.time()-start

		# See if operation works
		self.assertEqual(result['status'], 'ok')
		time_readout(inspect.stack()[0][0].f_code.co_name, dur, result['totalResults'])

	def test_top_search2(self):
		# get start time
		start = time.time()

		# Do Method operations
		result= search2(keyword)

		# calculate duration 
		dur = time.time()-start

		# See if operation works
		self.assertEqual(result['status'], 'ok')
		time_readout(inspect.stack()[0][0].f_code.co_name, dur, result['totalResults'])


if __name__ == '__main__':
	unittest.main()