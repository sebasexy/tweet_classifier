import csv
import nltk
import json
import random
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

documents = []
all_words = []
testing_documents = []
stop_words = set(stopwords.words('english'))

def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        if not w in stop_words:
            features[w] = (w in words)
    return features

def tokenize_tweet(tweet):
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


with open('tweets.json') as json_file:
    # csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    line_count = 0
    json_reader = json.load(json_file)
    word_list = list()

    for tweet in json_reader:
        if not tweet['gender'] == 2:
            res = tokenize_tweet(tweet['text'])
            word_list.append(res)
            word_list.append(tweet['gender'])
            documents.append(word_list)
            word_list = list()

    # for row in csv_reader:
    #     res = tokenize_tweet(row[0])
    #     word_list.append(res)
    #     word_list.append(row[1])
    #     documents.append(word_list)
    #     word_list = list()
        
        # if row[1] == 'Male':
        #     tokenize_tweet(row[0])
        #     line_count += 1
        # else:
        #     female_tweets.append(tokenize_tweet(row[0])
        #     line_count += 1
    
random.shuffle(documents)

for i in range(len(all_words)):
    all_words[i] = all_words[i].lower()

all_words = nltk.FreqDist(all_words)


word_features = list(all_words)

featuresets = [(find_features(tweet), category) for (tweet, category) in documents]

# TRAINING SET
training_set = featuresets[:840]

# TESTING SET
#testing_set = featuresets[820:840]

# PREDICTION SET
prediction_set = featuresets[840:]
prediction_set_features = [tweet for (tweet, category) in prediction_set]

# prediction_features = [(find_features(tweet)) for tweet in prediction_set]

# print("Length: ", len(prediction_set))

classifier = nltk.NaiveBayesClassifier.train(training_set)

predictions = classifier.classify_many(prediction_set_features)
predictions_real = [category for (tweet, category) in prediction_set]

equal = 0

for i in range(len(predictions)):
    if predictions[i] == predictions_real[i]:
        equal += 1

print("Accuracy: ", (equal*100)/len(predictions))

# print("Classify: ", classifier.classify_many(prediction_set_features))
# print("Classify:2", [category for (tweet, category) in prediction_set])

# print("Classifiers: ", classifier.classify_many(prediction_set))

# print("Classified: ", classifier.classify(prediction_features))


# print("Classifier Accuracy: ", nltk.classify.accuracy(classifier, training_set))
# print("Claassifier Accuracy: ", nltk.classify.accuracy(classifier, prediction_set))

dev_test_set = []

# classifier.show_most_informative_features(15)