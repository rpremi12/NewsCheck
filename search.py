from newsapi import NewsApiClient

def search(keyword):
	newsapi = NewsApiClient(api_key='ff1a3afb8cfd49de8cec580041662505')
	top_headlines = newsapi.get_top_headlines(q=keyword,
	                                        # category='business',
                                          language='en',
                                          country='us')

	return top_headlines

def search2(keyword):

	categories = ["entertainment", "general", "health" , "science" , "sports", "technology"]

	newsapi = NewsApiClient(api_key='ff1a3afb8cfd49de8cec580041662505')


	top_headlines = newsapi.get_top_headlines(q=keyword,
	                                         category='business',
                                          language='en',
                                          country='us')

	for cat in categories:
		temp = newsapi.get_top_headlines(q=keyword,
	                                         category=cat,
                                          language='en',
                                          country='us')
		if temp['totalResults'] >0 :
			top_headlines["articles"].append(temp['articles'])
			top_headlines['totalResults'] += temp['totalResults']

	return top_headlines


def search3(keyword, categ = 'business'):
	newsapi = NewsApiClient(api_key='ff1a3afb8cfd49de8cec580041662505')
	top_headlines = newsapi.get_top_headlines(q=keyword,
	                                       category= categ,
                                          language='en',
                                          country='us')

	return top_headlines


def search4(keyword, categ = 'business'):
	newsapi = NewsApiClient(api_key='ff1a3afb8cfd49de8cec580041662505')
	all_articles = newsapi.get_everything(q=keyword,
	                                      #sources='bbc-news,the-verge',
	                                      domains='bbc.co.uk,techcrunch.com',
	                                      from_param='2020-12-18',
	                                      to='2020-12-28',
	                                      language='en',
	                                      sort_by='relevancy',
	                                      page=2)

	return all_articles


def main():

	'''
	# Init
	newsapi = NewsApiClient(api_key='ff1a3afb8cfd49de8cec580041662505')


	# /v2/top-headlines
	top_headlines = newsapi.get_top_headlines(q='bitcoin',
	                                          #sources='bbc-news,the-verge',
	                                          category='business',
	                                          language='en',
	                                          country='us')

	# /v2/everything
	all_articles = newsapi.get_everything(q='bitcoin',
	                                      #sources='bbc-news,the-verge',
	                                      domains='bbc.co.uk,techcrunch.com',
	                                      from_param='2020-12-15',
	                                      to='2020-12-24',
	                                      language='en',
	                                      sort_by='relevancy',
	                                      page=2)

	# /v2/sources
	sources = newsapi.get_sources()
	print(search("iPhone"))

	pass
	'''
	print(search("Tesla"))
	pass

if __name__ == "__main__":
	main()