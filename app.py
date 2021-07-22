
from flask import Flask, request
from flask import render_template
from datetime import time

from sentiment import * 
from search import *
import sys
import math


import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import json

app = Flask(__name__)


def formatdata(score):
	return (score+1)/2

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


def get_week(keyword):
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
		mboth = round(mean(map(formatdata,total_both)),2)*100
		scores.append(round(mboth))
		


#	print(articles)
	#print(days)
	print("Scores of the week", scores)
	print(days)
	print(pos_articles)
	print(neu_articles)
	print(neg_articles)
	#print("Overall Score:", mean(total_both))

	calc2 = [ pos_articles[x] + neu_articles[x]  for x in range(7)]
	calc3 = [ pos_articles[x] + neu_articles[x] + neg_articles[x] for x in range(7)]
	print(calc2)
	#print(calc3)
	'''

	plt.bar(range(len(neg_articles)), neg_articles, tick_label=days)
	plt.bar(range(len(neu_articles)), neu_articles, bottom=neg_articles, tick_label=days)
	plt.bar(range(len(pos_articles)), pos_articles, bottom=calc2, tick_label=days)
	plt.legend(labels=['Negative','Neutral','Positive'])
	plt.xlabel("Analysis for found articles")
	plt.ylabel("% of total articles/headlines of a given sentiment")
	plt.title(str(days[6]) + " Past Week sentiment analysis for '"+keyword+"'")
	plt.show()

	'''

	response = {
	'maxscore': max(scores),
	'minscore': min(scores),
	'wscores': scores,
	'wdata': {

	'labels': days,
	'datasets': [{
	'label': '% Positive',
	'data': pos_articles,
	'pointRadius': 4,
	'backgroundColor': 
	'rgba(0, 210, 91,0.4)',

	'borderColor': 
	'rgba(0, 210, 91,0.8)',

	'borderWidth': 5,
	'fill':True
	},
	{
	'label': '% Neutral',
	'data': calc2,
	'pointRadius': 4,
	'backgroundColor': 
	'rgba(255, 171, 0,0.4)',

	'borderColor': 
	'rgb(255, 171, 0,0.8)',

	'borderWidth': 5,
	'fill':True
	},
	{
	'label': '% Negative',
	'data': [100,100,100,100,100,100,100],
	'pointRadius': 4,

	'backgroundColor': 
	'rgb(252, 66, 74,0.2)',

	'borderColor': 
	'rgb(252, 66, 74,0.8)',

	'borderWidth': 5,
	'fill':True
	}]}}
	print(response)
	return response

@app.route("/get_day")

def get_day():
	if request.method == "GET":
		keyword = request.args.get("q")
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
		return

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
	neu_articles = [format2(totalArticles, len([ x for x in total_score_body if x ==0])) , format2(totalArticles, len([ x for x in total_score_title if x == 0])),format2(totalArticles*2, len([ x for x in total_both if x== 0])) ]
	pos_articles = [format2(totalArticles, len([ x for x in total_score_body if x > 0])) , format2(totalArticles, len([ x for x in total_score_title if x > 0])), format2(totalArticles*2, len([ x for x in total_both if x > 0])) ]

	print(mean(map(formatdata, total_score_body)))
	print(mean(map(formatdata, total_score_title)))
	mboth = round(mean(map(formatdata,total_both)),2)*100
	print(mboth)
	
	print("neg:",neg_articles)
	print("neu:",neu_articles)
	print("pos:", pos_articles)

	print("Overall Score:", mboth)
	calc2 = [neg_articles[0] + neu_articles[0],neg_articles[1] + neu_articles[1], neg_articles[2]+neu_articles[2]]

	resp  = get_week(keyword)

	info={
	'maxscore': resp['maxscore'],
	'minscore': resp['minscore'],
	'wscores': resp['wscores'],
	'wdata': resp['wdata'],
	'dscore':round(mboth),
	'day_data': {
    'labels': ["Negative", "Positive","Neutral"],
    'datasets': [{
        'data': [round(neg_articles[2],1), round(pos_articles[2],1), round(neu_articles[2],1)],
        'backgroundColor': [
          "#FC424A","#00d25b","#ffab00"
        ]
      }
    ]}}

	return info
 
@app.route("/simple_chart")

def chart():
	legend = 'Monthly Data'
	labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
	values = [10, 9, 8, 7, 6, 4, 7, 8]
	print("REACED")
	return  {"name":legend}
	#render_template('chart.html', values=values, labels=labels, legend=legend)
	
if __name__ == "__main__":
	app.run(debug=True)
