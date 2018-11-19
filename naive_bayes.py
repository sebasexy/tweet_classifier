import nltk
import random
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import movie_reviews

def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features

# for category in movie_reviews.categories():
#     print(category)

documents = [(list(movie_reviews.words(fileid)), category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]
#print("Document: ", documents[3])
# documents = [("@MrLeon87892468 @PunishedUnicorn Listen - lots of ethnic categories exist. The Nazi Holocaust targeted Jews among o… https://t.co/ih666uUQgz",'Male'), ("Tomorrow’s game with the Saints will be the toughest game of the year. The Saints are well rounded and do some thin… https://t.co/OnOz5ABc0F",'Male'), ("@abc i think i got picked up by an auto chick .... like a bot ... something that likes you on twitter and then is r… https://t.co/FSt9K2KAmP",'Male'),
# ("@mgirdley Never doubted the decision. We would have given up too much, and there are plenty of other business prosp… https://t.co/87pCfqbmCV",'Male'),("@nnja @mariatta While I'm never thrilled to hear these statistics they are useful to serve as  baseline for a measu… https://t.co/dWVr94jYMA",'Female'),("Aircraft of choice is the B-2 Bomber because of its large body cross section enabling it to house a standard flying… https://t.co/Ge0OkxRaYX",'Female'),("Truer words have never been said Retired Army Guy, thank you! The time to be vigilant is upon us, now and for all e… https://t.co/y03XvHWxjI",'Female')]

random.shuffle(documents)

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

print(all_words)

all_words = nltk.FreqDist(all_words)

# print(all_words.most_common(15))

word_features = list(all_words.keys())[:3000]
featuresets = [(find_features(rev), category) for (rev, category) in documents]

ps = PorterStemmer()

EXAMPLE_TEXT = "Hello Mr. Smith, 'hi'c how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard. Eat Eating Eated Ponchiyo eats my sister's pussy"

word_tokens = word_tokenize(EXAMPLE_TEXT)

# for w in word_tokens:
#     print(ps.stem(w))

# print(word_tokens)