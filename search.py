from newsapi import NewsApiClient

def search(keyword, from_par="!", to_par="!"):
	newsapi = NewsApiClient(api_key='ff1a3afb8cfd49de8cec580041662505')
	top_headlines = newsapi.get_top_headlines(q=keyword,
	                                         category='business',
                                          language='en',
                                          country='us')

	#print(type(top_headlines))
	return top_headlines



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