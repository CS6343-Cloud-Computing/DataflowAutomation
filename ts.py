import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import string
import re
import sys

from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

sentiments = SentimentIntensityAnalyzer()
stop_words = set(stopwords.words('english'))

def clean_tweet(sentence):
	t= re.split(r"\s+|\\", sentence)
	filtered_t = []

	for i in range(1,len(t)):
		if(t[i].lower() not in stop_words):
			filtered_t.append(re.sub('[^A-Za-z0-9]+', '', t[i].lower()))

	return (filtered_t)

def sentiment_analyser(tweet_str):
	pos_val = [sentiments.polarity_scores(i)["pos"] for i in tweet_str.split(" ")]
	neg_val = [sentiments.polarity_scores(i)["neg"] for i in tweet_str.split(" ")]
	neu_val = [sentiments.polarity_scores(i)["neu"] for i in tweet_str.split(" ")]

	a = sum(pos_val)
	b = sum(neg_val)
	c = sum(neu_val)

	if (a>b) and (a>c):
		return "Positive"
	elif (b>a) and (b>c):
		return "Negative"
	else:
		return "Neutral"

sentence = " ".join(sys.argv[1:])
val = sentiment_analyser(sentence)
print(val)

