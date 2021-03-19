import unittest
import time
from search import *
import inspect
import sys 
import sentiment

keyword = "Tesla"

def time_readout(name, time , res):
	print(name,"| Elapsed time:", time, "| # of Articles:", res)

class TestSearchMethods(unittest.TestCase):
	'''
	def test_no_category_search(self):
		# get start time
		start = time.time()

		# Do Method operations
		result= search(keyword)

		# calculate duration 
		dur = time.time()-start

		# See if operation works
		self.assertEqual(result['status'], 'ok')
		time_readout(inspect.stack()[0][0].f_code.co_name, dur, result['totalResults'])


	def test_no_category_with_country_search(self):
		# get start time
		start = time.time()

		# Do Method operations
		result= search(keyword , 'us')

		# calculate duration 
		dur = time.time()-start

		# See if operation works
		self.assertEqual(result['status'], 'ok')
		time_readout(inspect.stack()[0][0].f_code.co_name, dur, result['totalResults'])




	def test_all_category_search(self):
		# get start time
		start = time.time()

		# Do Method operations
		result= search2(keyword)

		# calculate duration 
		dur = time.time()-start

		# See if operation works
		self.assertEqual(result['status'], 'ok')
		time_readout(inspect.stack()[0][0].f_code.co_name, dur, result['totalResults'])

	def test_all_category_with_country_search(self):
		# get start time
		start = time.time()

		# Do Method operations
		result= search2(keyword, 'us')

		# calculate duration 
		dur = time.time()-start

		# See if operation works
		self.assertEqual(result['status'], 'ok')
		time_readout(inspect.stack()[0][0].f_code.co_name, dur, result['totalResults'])




	def test_1_category_search(self):
		# get start time
		start = time.time()

		# Do Method operations
		result= search3(keyword)

		# calculate duration 
		dur = time.time()-start

		result2 = search3(keyword, "entertainment")

		# See if operation works
		self.assertEqual(result['status'], 'ok')
		self.assertEqual(result2['status'], 'ok')
		time_readout(inspect.stack()[0][0].f_code.co_name, dur, result['totalResults'])

	def test_1_category_with_country_search(self):
		# get start time
		start = time.time()

		# Do Method operations
		result= search3(keyword, country='us')

		# calculate duration 
		dur = time.time()-start

		result2 = search3(keyword, "entertainment", country='us')
		# See if operation works
		self.assertEqual(result['status'], 'ok')
		self.assertEqual(result2['status'], 'ok')
		time_readout(inspect.stack()[0][0].f_code.co_name, dur, result['totalResults'])



	def test_everything(self):
		# get start time
		start = time.time()

		# Do Method operations
		result = search4(keyword)

		# calculate duration 
		dur = time.time()-start

		# See if operation works
		self.assertEqual(result['status'], 'ok')
		time_readout(inspect.stack()[0][0].f_code.co_name, dur, result['totalResults'])
	

	def test_everything_recent(self):
		# get start time
		start = time.time()

		# Do Method operations
		result = search5(keyword)

		# calculate duration 
		dur = time.time()-start

		# See if operation works
		self.assertEqual(result['status'], 'ok')
		time_readout(inspect.stack()[0][0].f_code.co_name, dur, result['totalResults'])

	def test_google_search(self):
		# get start time
		start = time.time()

		# Do Method operations
		result = google_search(keyword)

		# calculate duration 
		dur = time.time()-start

		# See if operation works
		self.assertTrue(len(result)>0)
		time_readout(inspect.stack()[0][0].f_code.co_name, dur, -1)


	'''
	def test_sent_analysis_1(self):
		# get start time
		start = time.time()

		# Do Method operations
		result = sentiment.sentiment_score("They had the 'excuse' of lack of memory space with cartridges, but with the Switch, there is literally NO GOOD REASON to do that but CORPORATE GREED. That kind of practice shouldn't be allowed. Seriously, shame on you Nintendo!")

		# calculate duration 
		dur = time.time()-start
		print(result)

		# See if operation works
		self.assertTrue(result<0)
		time_readout(inspect.stack()[0][0].f_code.co_name, dur, -1)		


	def test_sent_analysis_2(self):
		# get start time
		start = time.time()

		# Do Method operations
		result = sentiment.sentiment_score_filtered("They had the 'excuse' of lack of memory space with cartridges, but with the Switch, there is literally NO GOOD REASON to do that but CORPORATE GREED. That kind of practice shouldn't be allowed. Seriously, shame on you Nintendo!")

		# calculate duration 
		dur = time.time()-start

		print(result)

		# See if operation works
		self.assertTrue(result<0)
		time_readout(inspect.stack()[0][0].f_code.co_name, dur, -1)		



	def test_sent_analysis_3(self):
		# get start time
		start = time.time()

		# Do Method operations
		result = sentiment.sentiment_score_sentence("They had the 'excuse' of lack of memory space with cartridges, but with the Switch, there is literally NO GOOD REASON to do that but CORPORATE GREED. That kind of practice shouldn't be allowed. Seriously, shame on you Nintendo!")

		# calculate duration 
		dur = time.time()-start

		print(result)

		# See if operation works
		self.assertTrue(result<0)
		time_readout(inspect.stack()[0][0].f_code.co_name, dur, -1)		


	def test_sent_analysis_4(self):
		# get start time
		start = time.time()

		# Do Method operations
		result = sentiment.sent_score("They had the 'excuse' of lack of memory space with cartridges, but with the Switch, there is literally NO GOOD REASON to do that but CORPORATE GREED. That kind of practice shouldn't be allowed. Seriously, shame on you Nintendo!")
		
		# calculate duration 
		dur = time.time()-start

		print(result)
		#result = result["mean_compound"]-1 

		# See if operation works
		self.assertTrue(result=="neg")
		time_readout(inspect.stack()[0][0].f_code.co_name, dur, -1)		

	def test_sent_analysis_5(self):
		# get start time
		start = time.time()

		# Do Method operations
		result = sentiment.sent_score("This is the best game I have ever played! It is amazing!")
		
		# calculate duration 
		dur = time.time()-start

		print(result)
		#result = result["mean_compound"]-1 

		# See if operation works
		self.assertTrue(result=="neg")
		time_readout(inspect.stack()[0][0].f_code.co_name, dur, -1)		



if __name__ == '__main__':
	unittest.main()