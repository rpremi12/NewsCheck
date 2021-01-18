from newsapi import NewsApiClient
from datetime import datetime, timedelta


def search(keyword, country = None):
	newsapi = NewsApiClient(api_key='ff1a3afb8cfd49de8cec580041662505')
	top_headlines ={}
	if country == None:
		top_headlines = newsapi.get_top_headlines(q=keyword,
	                                        # category='business',
                                          language='en')
	else:
		top_headlines = newsapi.get_top_headlines(q=keyword,
                                    # category='business',
                                  language='en',
                                  country=country)

	return top_headlines

def search2(keyword, country = None):

	categories = ["entertainment", "general", "health" , "science" , "sports", "technology"]

	newsapi = NewsApiClient(api_key='ff1a3afb8cfd49de8cec580041662505')

	top_headlines = {}

	if country ==None:
		top_headlines = newsapi.get_top_headlines(q=keyword,
		                                         category='business',
	                                          language='en')
	else:
		top_headlines = newsapi.get_top_headlines(q=keyword,
		                                         category='business',
	                                          language='en',
	                                          country=country)
	 		

	for cat in categories:
		if country ==None:
			temp = newsapi.get_top_headlines(q=keyword,
		                                         category=cat,
	                                          language='en' )
		else:
			temp = newsapi.get_top_headlines(q=keyword,
		                                         category=cat,
	                                          language='en',
	                                          country=country )
		if temp['totalResults'] >0 :
			top_headlines["articles"].append(temp['articles'])
			top_headlines['totalResults'] += temp['totalResults']

	return top_headlines


def search3(keyword, categ = 'business', country= None):
	newsapi = NewsApiClient(api_key='ff1a3afb8cfd49de8cec580041662505')
	if country ==None:
		top_headlines = newsapi.get_top_headlines(q=keyword,
		                                       category= categ,
	                                          language='en')
	else:
		top_headlines = newsapi.get_top_headlines(q=keyword,
		                                       category= categ,
	                                          language='en',
	                                          country =country)		

	return top_headlines


def search4(keyword, from_par = '2020-12-19', to_par ='2021-01-17'):
	newsapi = NewsApiClient(api_key='ff1a3afb8cfd49de8cec580041662505')
	all_articles = newsapi.get_everything(q=keyword,
	                                      #sources='bbc-news,the-verge',
	                                     # domains='bbc.co.uk,techcrunch.com',
	                                      from_param=from_par,
	                                      to=to_par,
	                                      language='en',
	                                      sort_by='relevancy',
	                                      page=1)

	return all_articles

def search5(keyword):
	newsapi = NewsApiClient(api_key='ff1a3afb8cfd49de8cec580041662505')

	got = datetime.now() - timedelta(days =1)

	all_articles = newsapi.get_everything(q=keyword,
	                                      #sources='bbc-news,the-verge',
	                                     # domains='bbc.co.uk,techcrunch.com',
	                                      from_param=got.strftime('%Y-%m-%dT%H:%M:%S'),
	                                      to=datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
	                         
	                                      language='en',
	                                      sort_by='popularity',
	                                      page=1)

	return all_articles


def main():

	sources = newsapi.get_sources()

	print(search("Tesla"))
	pass

if __name__ == "__main__":
	main()