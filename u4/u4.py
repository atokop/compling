# -*- coding: utf-8 -*-
from __future__ import division
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import textutils
from nltk.corpus import brown, reuters, state_union, words
from small_analysis import yoursmall_words, yoursmall_words_lem, yoursmall_sents
import utils

# tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
def load_words(filename):
    f=open(filename,'rU')
    raw=f.read()
    tokens = word_tokenize(raw)
    return tokens

def load_clean_words(filename):
    utils.clean(load_words(filename))

# Returns a feature set with boolean values for whether the document contains
# each of the words given.
def word_existence_feature_set(feature_words, document_words):
    words = set(feature_words)
    features = {}
    for word in words:
        features['contains(%s)' % word] = word in document_words
    return features

def top_words_by_frequency(words, n=20):
    return nltk.FreqDist(words).keys()[:n]

def top_words_with_frequency(words, n=20):
    return nltk.FreqDist(words).items()[:n]
