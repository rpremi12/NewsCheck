import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

unwanted = nltk.corpus.stopwords.words("english")
unwanted.extend([w.lower() for w in nltk.corpus.names.words()])


def skip_unwanted(word):
    if not word.isalpha() or word in unwanted:
        return False
    return True

sia = SentimentIntensityAnalyzer()



def sentiment_score_filtered(string):
	string = " ".join([w for w in string.split(" ") if skip_unwanted(w) == True])
	compound = sia.polarity_scores(string)["compound"]
	print(sia.polarity_scores(string))
	return compound

def sentiment_score(string):
	compound = sia.polarity_scores(string)["compound"]
	print(sia.polarity_scores(string))

	return compound

