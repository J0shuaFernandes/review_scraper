from nltk.corpus import movie_reviews
from nltk import FreqDist
from random import shuffle

documents = [(list(movie_reviews.words(fileid)), category)
			for category in movie_reviews.categories()
			for fileid in movie_reviews.fileids(category)]
print(documents[1])
print(len(documents))
shuffle(documents)

all_words = []
for w in movie_reviews.words():
	all_words.append(w.lower())
#print(all_words[:10])
word_features = list(all_words)[:3000]

def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features

#print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))
featuresets = [(find_features(rev), category) for (rev, category) in documents]

training_set = featuresets[:1900]
testing_set = featuresets[1900:]
print(training_set[0])

classifier = NaiveBayesClassifier.train(training_set)
print('Accuracy: ', (nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_informative_features(15)

clf = open('naivebayes.pkl', 'wb')
pickle.dump(classifier, clf)
clf.close()