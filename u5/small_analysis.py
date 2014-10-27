# -*- coding: utf-8 -*-
from __future__ import division
import nltk
#from nltk.book import *
import dateutil
import pyparsing
import numpy
import six
import matplotlib
from nltk.corpus import PlaintextCorpusReader
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import brown, reuters, state_union, words
import utils

# Put your corpus directory path below instead, e.g.” D:\Test\ClassEvents” 
corpus_root = '/Users/kwamina/school_dev/senior/comp_linguistics/corpus_small/'
classevent_corpus_root = '/Users/kwamina/school_dev/senior/comp_linguistics/Islip13Rain'
big_corpus_root = '/Users/kwamina/school_dev/senior/comp_linguistics/YourBigRel'
yoursmall_wordlists = PlaintextCorpusReader(corpus_root, '.*')
classevent_wordlists = PlaintextCorpusReader(classevent_corpus_root, '.*')
big_wordlists = PlaintextCorpusReader(big_corpus_root, '.*')

# The next step is to show the file names under the directory (optional step)
lemmer = WordNetLemmatizer()

def clean_words(words):
    words = [w.lower() for w in words if w.isalnum()]
    return words

def clean_sents(sents):
    return [clean_words(sent) for sent in sents]

    
classevent_words = classevent_wordlists.words()
classevent_sents = classevent_wordlists.sents()
classevent_words = [w.lower() for w in classevent_words if w.isalnum()]
classevent_words = nltk.Text(classevent_words)
classevent_words_lem = [lemmer.lemmatize(w) for w in classevent_words]
print "ClassEvent loaded"

yoursmall_words = yoursmall_wordlists.words()
yoursmall_sents = yoursmall_wordlists.sents()
yoursmall_words = [w.lower() for w in yoursmall_words if w.isalnum()]
yoursmall_words = nltk.Text(yoursmall_words)
yoursmall_words_lem = [lemmer.lemmatize(w) for w in yoursmall_words]
print "YourSmall loaded"

big_words = big_wordlists.words()
big_sents = big_wordlists.sents()
big_words = [w.lower() for w in big_words if w.isalnum()]
big_words = nltk.Text(big_words)
big_words_lem = [lemmer.lemmatize(w) for w in big_words]
print "Big loaded"

yourwords = ['earthquake', 'seismic', 'aftershocks', 'quake', 'damage', 'magnitude', 'tremor', 'richter', 'epicenter', 'depth', 'fault', 'hypocenter', 'focus', 'dead', 'casualties', 'structural', 'seismometer', 'temblor', 'hazard', 'impact']
yourwords_lem = [lemmer.lemmatize(w.lower()) for w in yourwords]


#baseline_words = brown.words() + state_union.words() + reuters.words() + words.words()
#baseline_words_lem = [lemmer.lemmatize(w) for w in baseline_words]
#print "Baseline loaded"

def non_cumulative_word_length_distribution(words):
    freq_dist_pairs = FreqDist([len(w) for w in words]).items()
    return_dist = {}
    for pair in freq_dist_pairs:
        return_dist[pair[0]] = pair[1]
    return return_dist

def cumulative_word_length_distribution(words):
    non_cumulative_dist = non_cumulative_word_length_distribution(words)
    print non_cumulative_dist
    cumulative_dist = {}
    for i in non_cumulative_dist:
        sum = 0
        for j in range(i):
            k = j + 1
            if k not in non_cumulative_dist:
                continue
            sum += non_cumulative_dist[k]
        cumulative_dist[i] = sum
    return cumulative_dist

def relative_frequency(word, set_of_words, *args):
    if (args):
        length = float(args[0])
    else:
        length = float(len(set_of_words))

    return float(FreqDist(set_of_words)[word]) / length

def rel_freqs_from_set(words_to_check, set_of_words, *args):
    return_dict = {}
    if (args):
        length = float(args[0])
    else:
        length = float(len(set_of_words))
    for word in words_to_check:
        return_dict[word] = relative_frequency(word, set_of_words, length)
    return return_dict

