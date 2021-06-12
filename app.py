
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
	mboth = mean(map(formatdata,total_both))
	mboth = round(mboth*10, 1)
	print(mboth)
	
	print("neg:",neg_articles)
	print("neu:",neu_articles)
	print("pos:", pos_articles)

	print("Overall Score:", mboth)
	calc2 = [neg_articles[0] + neu_articles[0],neg_articles[1] + neu_articles[1], neg_articles[2]+neu_articles[2]]

	info=
	{'day_data': {
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
