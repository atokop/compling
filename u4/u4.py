# -*- coding: utf-8 -*-
from __future__ import division
from unidecode import unidecode
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import brown, reuters, state_union, words
from small_analysis import yoursmall_words, yoursmall_words_lem, yoursmall_sents
import utils
import os
import random

training_dir = "/Users/kwamina/compling/YourSmallTrain/"
def load_words(filename):
    f=open(filename,'rU')
    raw=unidecode(f.read())
    tokens = word_tokenize(raw)
    return tokens

def load_clean_words(filename):
    utils.clean(load_words(filename))

# Returns a feature set with boolean values for whether the document contains
# each of the words given.
def contains_word_feature_set(document_words, feature_words):
    features = {}
    document_words = [w.lower() for w in document_words]

    for word in feature_words:
        features['contains(%s)' % word] = word in document_words
    return features

def contains_word_feature_set_from_file(filename, feature_words):
    document_words = set(utils.ascii_clean(load_words(filename)))
    return contains_word_feature_set(document_words, feature_words)

def top_words_by_frequency(words, n=20):
    return [word[0] for word in nltk.FreqDist(words).most_common()[:n]]

def top_words_with_frequency(words, n=20):
    return nltk.FreqDist(words).items()[:n]

def create_boolean_training_sets(create_featureset_func, tagged_dir):
    files = os.listdir(tagged_dir)
    pos_files = [f for f in os.listdir(tagged_dir) if f[-8:] == "_pos.txt"]
    neg_files = [f for f in os.listdir(tagged_dir) if f[-8:] == "_neg.txt"]

    tagged_set = []
    for f in pos_files:
        tagged_set.append((create_featureset_func(tagged_dir+f), True))
    for f in neg_files:
        tagged_set.append((create_featureset_func(tagged_dir+f), False))

    random.shuffle(tagged_set)
    fraction = 0.75
    training_set = tagged_set[:int(len(tagged_set) * fraction)]
    test_set = tagged_set[int(len(tagged_set) * fraction):]
    return (training_set, tagged_set)
