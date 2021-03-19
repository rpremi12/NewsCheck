import re
import pandas as pd
from sklearn.model_selection import train_test_split
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense, Conv1D, MaxPooling1D, Flatten, Embedding
import numpy as np
import os
from keras.preprocessing.sequence import pad_sequences
import sys


# A small pre-processing function to clean up
def clean_review(text):
    # Strip HTML tags
    text = re.sub('<[^<]+?>', ' ', text)
    text = text.replace('\\"', '')
    text = text.replace('"', '')
    text = re.sub(r'[\r\n]',' ',text)
    text = re.sub(r'[\.!?,:] *', '. ', text)
    return text.strip()


def clean_score(num):
	if num > 10:
		num = num/10

	if num<=5 :
		return 0
	elif num==5 or num==6:
		return 0.5
	else:
		return 1
	
def to_sequence(tokenizer, preprocessor, index, text):
    words = tokenizer(preprocessor(text))
    indexes = [index[word] for word in words if word in index]
    return indexes


def fill_set(str1='data/mc_training.csv', str2='data/mc_testing.csv'):

	df2 = pd.read_csv(str1)
	df3 = pd.read_csv(str2)

	#create cleaned review, which is every "review" entry passed through the clean_review function above

	df2['cleaned_review'] = df2['body'].apply(clean_review)
	df2['sentiment'] = df2['score'].apply(clean_score)

	df3['cleaned_review'] = df3['body'].apply(clean_review)
	df3['sentiment'] = df3['score'].apply(clean_score)

	#create test and training sets with a split
	#X_train, X_test, y_train, y_test = train_test_split(df['cleaned_review'], df['sentiment'], test_size=0.3)

	return 	(df2['cleaned_review'], df3['cleaned_review'], df2['sentiment'], df3['sentiment'])



class sentMod:


	def sequence_setup(self, X_train):

		self.vectorizer = CountVectorizer(binary=True, stop_words=stopwords.words('english'), min_df=3, max_df=0.9, max_features=None)

		X_train_onehot = self.vectorizer.fit_transform(X_train)

		#They take word-ids as input, so we first have to transform the input into a series of word ids
		self.word2idx = {word: idx for idx, word in enumerate(self.vectorizer.get_feature_names())}
		self.tokenize = self.vectorizer.build_tokenizer()
		self.preprocess = self.vectorizer.build_preprocessor()
		 
		X_train_sequences = [to_sequence(self.tokenize, self.preprocess, self.word2idx, x) for x in X_train]

		self.MAX_SEQ_LENGHT = len(max(X_train_sequences, key=len))
		self.N_FEATURES = len(self.vectorizer.get_feature_names())

		X_train_sequences = pad_sequences(X_train_sequences, maxlen=self.MAX_SEQ_LENGHT, value=self.N_FEATURES)

		return  X_train_sequences


	def create_model(self):

		# load training data
		X_train, X_test, y_train, y_test = fill_set()
		# setup preprocessing tools for embeddings
		X_train_sequences= self.sequence_setup(X_train)

		#Prepare model
		self.model = Sequential()

		self.model.add(Embedding(len(self.vectorizer.get_feature_names()) + 1, 64, input_length=self.MAX_SEQ_LENGHT))
		self.model.add(Conv1D(64, 5, activation='relu'))
		self.model.add(MaxPooling1D(5))
		self.model.add(Flatten())
		self.model.add(Dense(units=500, activation='relu', input_dim=len(self.vectorizer.get_feature_names())))
		self.model.add(Dense(units=1, activation='sigmoid'))
		
		self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
		self.model.summary()

		self.model.fit(X_train_sequences[:-100], y_train[:-100], epochs=3, batch_size=512, verbose=1,   validation_data=(X_train_sequences[-100:], y_train[-100:]))

		# Test the out accuracy
		print("Accuracy:", self.get_accuracy()) 

		# Save the model to the disk
		self.model.save(f'sentimentModel')
		print('Sentiment Model Saved to Disk!')


	def __init__(self, training= "data/mc_training.csv", testing="data/mc_testing.csv"):

		if os.path.exists("sentimentModel/") == False:
			self.create_model()
		else:
			X_train = fill_set(training, testing)[0]
			self.sequence_setup(X_train)
			self.model = load_model("sentimentModel/")
			self.get_accuracy()

	def format_predict( self, data):
		temp_sequences = [to_sequence(self.tokenize, self.preprocess, self.word2idx, x) for x in data]
		temp_sequences = pad_sequences(temp_sequences, maxlen=self.MAX_SEQ_LENGHT, value=self.N_FEATURES)
		return temp_sequences

	def get_accuracy(self):
		x, X_test,y, y_test = fill_set()
		X_test_sequences = self.format_predict( X_test)
		scores = self.model.evaluate(X_test_sequences, y_test, verbose=1)
		self.accuracy = scores[1]
		return scores[1]

	def get_results(self):
		x, X_test,y, y_test = fill_set()
		predictions = self.model.predict(self.format_predict(X_test))
		result= []
		for pred in predictions:
			result.append(pred[0])
		return result


	def predict(self, tests, pretty=False):
		if pretty == False:
			return self.model.predict(self.format_predict(tests))
		else:
			predictions = self.model.predict(self.format_predict(tests))
			i =0
			#print(len(predictions))
			for pred in predictions:
				print(tests[i] +": " + str(pred[0]))
				i+=1


def main():

	sent_tester =  sentMod()

	print(sent_tester.predict([" I love this game, it's the best I have ever played!" ,"I hate this game, it's the worst I have ever played!", "Devil may cry"]))

if __name__ == '__main__':
	main()