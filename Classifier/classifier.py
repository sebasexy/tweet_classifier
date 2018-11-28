import nltk
import random
import json
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import movie_reviews

class Classifier:
    naiveBayes = None

    def classify(self, text):
        global naiveBayes
        tokens = []
        if naiveBayes is None:
            return 0

        tweet = self.tokenize_tweet(text,tokens)
        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()
        
        word_features = list(tokens)

        featureset = self.find_features(tweet,tokens)

        frequencies = nltk.FreqDist(tokens)
        return naiveBayes.classify(featureset)
        
    def initialize(self):
        global naiveBayes
        with open('tweets.json') as json_file:
            line_count = 0
            json_reader = json.load(json_file)
            word_list = list()

            all_words = []
            documents = []
            for tweet in json_reader:
                if not tweet['gender'] == 2:
                    res = self.tokenize_tweet(tweet['text'], all_words)
                    word_list.append(res)
                    word_list.append(tweet['gender'])
                    documents.append(word_list)
                    word_list = list()
            
        random.shuffle(documents)

        for i in range(len(all_words)):
            all_words[i] = all_words[i].lower()

        all_words = nltk.FreqDist(all_words)
 

        word_features = list(all_words)

        featuresets = [(self.find_features(tweet, word_features), category) for (tweet, category) in documents]

        # TRAINING SET
        training_set = featuresets

        naiveBayes = nltk.NaiveBayesClassifier.train(training_set)

    def tokenize_tweet(self, tweet, all_words):
        res = word_tokenize(tweet)
        
        clean_tweet = list()

        for i in range(len(res)):
            if i > 1 and (res[i-2] == 'https' or res[i-2] == 'http') and res[i-1] == ':':
                continue
            elif i>0 and (not res[i] == '@' and not res[i-1] == '@') :
                clean_tweet.append(res[i])
                all_words.append(res[i])
            elif i==0 and (not res[i] == '@'):
                clean_tweet.append(res[i])
                all_words.append(res[i])
            elif res[i] == 'https' or res[i] == 'http':
                continue
            elif res[i] == '#':
                continue            
            elif i > 0 and (res[i] == ':' and (res[i-1] == 'https' or res[i-1] == 'http')):
                continue
        return clean_tweet

    def find_features(self, document, word_features):
        stop_words = set(stopwords.words('english'))
        words = set(document)
        features = {}
        for w in word_features:
            if not w in stop_words:
                features[w] = (w in words)
        return features