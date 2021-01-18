import unittest
import time
from search import *
import inspect


def time_readout(name, time):
	print(name,"| Elapsed time:", time)

class TestSearchMethods(unittest.TestCase):


	def test_top_search(self):
		start = time.time()

		result= search("Tesla")
		#print(result)
		self.assertEqual(result['status'], 'ok')

		dur = time.time()-start
		time_readout(inspect.stack()[0][0].f_code.co_name, dur)

	'''
	def test_upper(self):
		start = time.time()

		self.assertEqual('foo'.upper(), 'FOO')

		dur = time.time()-start
		time_readout(inspect.stack()[0][0].f_code.co_name, dur)



	def test_isupper(self):
		start = time.time()

		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())

		dur = time.time()-start
		time_readout(inspect.stack()[0][0].f_code.co_name,  dur)


	def test_split(self):
		start = time.time()

		s = 'hello world'
		self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
		with self.assertRaises(TypeError):
			s.split(2)

		dur = time.time()-start
		time_readout(inspect.stack()[0][0].f_code.co_name, dur)
	'''

if __name__ == '__main__':
	unittest.main()