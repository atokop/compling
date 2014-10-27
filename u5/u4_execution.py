import u4
import utils
import os
import random
import nltk

tagged_dir = "/Users/kwamina/compling/YourSmallTrain/"

# Creates set of words to use as features for each document based on most common words in corpus.
feature_words = set(u4.top_words_by_frequency(utils.ascii_clean(u4.yoursmall_words), 15))

# Creates a featureset for a document by determining the presence of common words in the document.
def create_featureset(filename):
    return u4.contains_word_feature_set_from_file(filename, feature_words)

# Trains a naive bayes classifier using the featureset function defined.
training_set, test_set = u4.create_boolean_training_sets(create_featureset, tagged_dir)

decision_tree = nltk.DecisionTreeClassifier.train(training_set)
bayes = nltk.NaiveBayesClassifier.train(training_set)

print "decision tree accuracy: %s" % nltk.classify.accuracy(decision_tree, test_set)
print "bayes accuracy: %s" % nltk.classify.accuracy(bayes, test_set)
