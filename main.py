from sentiment import * 
from search import *
import sys
import math


import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt


def formatdata():
	pass

def getInput():
	timeframe = "d"
	keyword = ""

	while True:
		print("Usage: (d)ay, (w)eek, (m)onth, (q)uit")
		timeframe = input("Enter Time Range here:")
		if timeframe in ["d","w","m"]:
			break
		elif timeframe == "q":
			sys.exit(1)
		else:
			continue

	while True:
		keyword = input("Enter a keyword to search for:")
		if not keyword.replace(' ','').isalpha():
			print("Enter a word")	
			continue
		else:
			break

	return (timeframe, keyword)

def format2(total, num):
	#print(total,num)
	return float(100)*(float(total)-(float(total)-float(num)))/float(total)

def main():

	print("News Check 0.05:\n")

	while True:
		timeframe, keyword = getInput()

		if timeframe =="d":
			curr_day = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
			prev_day =( datetime.now() - timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%S')
			curr_week =( datetime.now() - timedelta(days=7)).strftime('%Y-%m-%dT%H:%M:%S')

			articles = search4(keyword, prev_day, curr_day )
			#print(articles)

			totalArticles = articles["totalResults"]

			if totalArticles >= 20:
				totalArticles = 20
			elif totalArticles ==0:
				print("no results found")
				continue

			articles = articles['articles'][:totalArticles]
			total_score_body = []
			total_score_title = []
			total_both = []


			for art in articles:
				total_score_title.append(sentiment_score_filtered(art['title']))
				if art['content'] != None:
					total_score_body.append(sentiment_score_filtered(art['content']))
				else:
					total_score_body.append(0.0)

			total_both = list(total_score_body)
			total_both.extend(total_score_title)


			neg_articles = [format2(totalArticles, len([ x for x in total_score_body if x < 0])) , format2(totalArticles, len([ x for x in total_score_title if x < 0])),format2(totalArticles*2, len([ x for x in total_both if x < 0])) ]
			neu_articles = [format2(totalArticles, len([ x for x in total_score_body if x ==0])) , format2(totalArticles, len([ x for x in total_score_title if x == 0])),format2(totalArticles*2, len([ x for x in total_both if x== 0]))  ]
			pos_articles = [format2(totalArticles, len([ x for x in total_score_body if x > 0])) , format2(totalArticles, len([ x for x in total_score_title if x > 0])), format2(totalArticles*2, len([ x for x in total_both if x > 0])) ]

			'''
			print(mean(total_score_body))
			print(mean(total_score_title))
			print(mean(total_both))
			

			print("neg:",neg_articles)
			print("neu:",neu_articles)
			print("pos:", pos_articles)
			'''

			print("Overall Score:", mean(total_both))
			calc2 = [neg_articles[0] + neu_articles[0],neg_articles[1] + neu_articles[1], neg_articles[2]+neu_articles[2]]


			plt.bar(range(len(neg_articles)), neg_articles, tick_label=['body','title','both'])
			plt.bar(range(len(neu_articles)), neu_articles, bottom=neg_articles, tick_label=['body','title','both'])
			plt.bar(range(len(pos_articles)), pos_articles, bottom=calc2, tick_label=['body','title','both'])
			plt.legend(labels=['Negative','Neutral','Positive'])
			plt.xlabel("Analysis for found articles")
			plt.ylabel("% of total articles/headlines of a given sentiment")
			plt.title(str(curr_week) + " sentiment analysis for '"+keyword+"'")
			plt.show()

		if timeframe =='w':

			neg_articles =[]
			neu_articles =[]
			pos_articles =[]
			days = []
			scores = []

			for day in range(7):				
				curr_day = (datetime.now()- timedelta(days=6-day)).strftime('%Y-%m-%dT%H:%M:%S')
				days.append((datetime.now()- timedelta(days=6-day)).strftime('%Y-%m-%d'))

				prev_day =( datetime.now() - timedelta(days=7-day)).strftime('%Y-%m-%dT%H:%M:%S')
				curr_week =( datetime.now() - timedelta(days=13-day)).strftime('%Y-%m-%dT%H:%M:%S')

				articles = search4(keyword, prev_day, curr_day )
				#print(articles)
				
				
				totalArticles = articles["totalResults"]

				if totalArticles >= 20:
					totalArticles = 20
				elif totalArticles ==0:
					print("no results found")
					continue

				articles = articles['articles'][:totalArticles]
				total_score_body = []
				total_score_title = []
				total_both = []


				for art in articles:
					total_score_title.append(sentiment_score_filtered(art['title']))
					if art['content'] != None:
						total_score_body.append(sentiment_score_filtered(art['content']))
					else:
						total_score_body.append(0.0)

				total_both = list(total_score_body)
				total_both.extend(total_score_title)

				neg_articles.append(format2(totalArticles*2, len([ x for x in total_both if x < 0])))
				neu_articles.append(format2(totalArticles*2, len([ x for x in total_both if x== 0])))
				pos_articles.append(format2(totalArticles*2, len([ x for x in total_both if x > 0])))
				scores.append(mean(total_both))
				


		#	print(articles)
			#print(days)
			print("Scores of the week", scores)
			#print("Overall Score:", mean(total_both))
			
			calc2 = [ neu_articles[x] + neg_articles[x] for x in range(7)]

			plt.bar(range(len(neg_articles)), neg_articles, tick_label=days)
			plt.bar(range(len(neu_articles)), neu_articles, bottom=neg_articles, tick_label=days)
			plt.bar(range(len(pos_articles)), pos_articles, bottom=calc2, tick_label=days)
			plt.legend(labels=['Negative','Neutral','Positive'])
			plt.xlabel("Analysis for found articles")
			plt.ylabel("% of total articles/headlines of a given sentiment")
			plt.title(str(days[6]) + " Past Week sentiment analysis for '"+keyword+"'")
			plt.show()
		







if __name__ == '__main__':
	main()