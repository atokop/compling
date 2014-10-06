# -*- coding: utf-8 -*-
from __future__ import division
import nltk
import textutils
from nltk.corpus import brown, reuters, state_union, words
from small_analysis import yoursmall_words, yoursmall_words_lem, yoursmall_sents

# Returns a feature set with boolean values for whether the document contains
# each of the words given.
def word_existence_feature_set(feature_words, document_words):
    words = set(feature_words)
    features = {}
    for word in words:
        features['contains(%s)' % word] = word in document_words)
    return features

def top_words_by_frequency(words, n=20):
    return nltk.FreqDist(words).keys()[:n]

def top_words_with_frequency(words, n=20):
    return nltk.FreqDist(words).items()[:n]
