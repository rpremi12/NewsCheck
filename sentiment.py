import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize
from sklearn.neural_network import MLPClassifier
from statistics import mean
from random import shuffle
import pickle as cPickle

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
	#print(sia.polarity_scores(string))
	return compound

def sentiment_score(string):
	compound = sia.polarity_scores(string)["compound"]
	#print(sia.polarity_scores(string))

	return compound

def sentiment_score_sentence(string):
	pop_scores = {'neg': 0.0, 'neu': 0.0, 'pos': 0.0 , 'compound': 0.0}
	sents = sent_tokenize(string)
	for s in sents:
		scores = sia.polarity_scores(string)
		pop_scores["compound"] += scores["compound"]
		pop_scores["neg"] += scores["neg"]
		pop_scores["neu"] += scores["neu"]
		pop_scores["pos"] += scores["pos"]


	#print(pop_scores)

	return pop_scores['compound']/len(sents)


def skip_unwanted2(pos_tuple):

    word, tag = pos_tuple

    if not word.isalpha() or word in unwanted:

        return False

    if tag.startswith("NN"):

        return False

    return True
'''
positive_words = [word for word, tag in filter(

    skip_unwanted2,

    nltk.pos_tag(nltk.corpus.movie_reviews.words(categories=["pos"]))

)]

negative_words = [word for word, tag in filter(

    skip_unwanted2,

    nltk.pos_tag(nltk.corpus.movie_reviews.words(categories=["neg"]))

)]


positive_fd = nltk.FreqDist(positive_words)
negative_fd = nltk.FreqDist(negative_words)

common_set = set(positive_fd).intersection(negative_fd)

for word in common_set:
    del positive_fd[word]
    del negative_fd[word]

top_100_positive = {word for word, count in positive_fd.most_common(200)}
top_100_negative = {word for word, count in negative_fd.most_common(200)}
'''
with open('100pos.pkl', 'rb') as fid:
    top_100_positive = cPickle.load(fid)

with open('100neg.pkl', 'rb') as fid:
    top_100_negative = cPickle.load(fid)



def extract_features(text):
    features = dict()
    wordcount = 0
    compound_scores = list()
    positive_scores = list()
    negative_scores = list()


    for sentence in nltk.sent_tokenize(text):
        for word in nltk.word_tokenize(sentence):
            if word.lower() in top_100_positive:
                wordcount += 1
            if word.lower() in top_100_negative:
                wordcount += 1
        compound_scores.append(sia.polarity_scores(sentence)["compound"])
        positive_scores.append(sia.polarity_scores(sentence)["pos"])
        negative_scores.append(sia.polarity_scores(sentence)["neg"])


    # Adding 1 to the final compound score to always have positive numbers
    # since some classifiers you'll use later don't work with negative numbers.
    features["mean_compound"] = mean(compound_scores) + 1
    features["mean_positive"] = mean(positive_scores)
    features["mean_negative"] = mean(negative_scores)

    features["wordcount"] = wordcount

    return features
'''
features = [
    (extract_features(nltk.corpus.movie_reviews.raw(review)), "pos")
    for review in nltk.corpus.movie_reviews.fileids(categories=["pos"])
]
features.extend([
    (extract_features(nltk.corpus.movie_reviews.raw(review)), "neg")
    for review in nltk.corpus.movie_reviews.fileids(categories=["neg"])
])


train_count = len(features) // 4
shuffle(features)
classifier = nltk.NaiveBayesClassifier.train(features[:train_count])
classifier.show_most_informative_features(10)
print(nltk.classify.accuracy(classifier, features[train_count:]))
with open('my_dumped_classifier.pkl', 'wb') as fid:
    cPickle.dump(classifier, fid) 
with open('100pos.pkl', 'wb') as fid:
    cPickle.dump(top_100_positive, fid)    
with open('100neg.pkl', 'wb') as fid:
    cPickle.dump(top_100_negative ,fid)      
'''
 


with open('my_dumped_classifier.pkl', 'rb') as fid:
    classifier = cPickle.load(fid)

def sent_score(string):

	string =classifier.classify(extract_features(string))
	#  print(string)
	return string

#print(sent_score("They had the 'excuse' of lack of memory space with cartridges, but with the Switch, there is literally NO GOOD REASON to do that but CORPORATE GREED. That kind of practice shouldn't be allowed. Seriously, shame on you Nintendo!"))