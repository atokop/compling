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
import small_analysis
import textutils
import trigram_tagging

def tagged_nouns(tagged_words):
    return remove_stopwords_tagged(textutils.findtags("NN", tagged_words))

stopset = set(nltk.corpus.stopwords.words('english'))
f = open("./stopwords.txt", "r")
for line in f.readlines():
    word = line.strip()
    if word not in stopset:
        stopset.add(word)
       # print "%s added to stopset" % (word)

def brown_tagged_sents():
    from nltk.corpus import brown
    brown_tagged_sents = brown.tagged_sents(categories='news')
    brown_sents = brown.sents(categories='news')
    unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
    size = int(len(brown_tagged_sents) * 0.9)
    train_sents = brown_tagged_sents[:size]
    return (train_sents, brown_tagged_sents[size:])

def remove_stopwords_tagged(tagged):
    out = [(word_with_tag[0], word_with_tag[1]) for word_with_tag in tagged if word_with_tag[0] not in stopset]
    return out

def simple_pos_tag(words):
    tagged = nltk.pos_tag(words)
    print "tagging complete, removing stopwords"
    tagged_without_stopwords =  [(word_with_tag[0], word_with_tag[1]) for word_with_tag in tagged if word_with_tag[0] not in stopset and str.isalpha(word_with_tag[0])]
    print "stopwords removed"
    tagged_without_dups = list(set(tagged_without_stopwords))
    sorted_tagged_without_dups = sorted(tagged_without_dups, key=lambda x: x[0])
    return sorted_tagged_without_dups

def get_regexp_tagger():
    patterns = [
        (r'.*ing$', 'VBG'),               # gerunds
        (r'.*ed$', 'VBD'),                # simple past
        (r'.*es$', 'VBZ'),                # 3rd singular present
        (r'.*ould$', 'MD'),               # modals
        (r'.*\'s$', 'NN$'),               # possessive nouns
        (r'.*s$', 'NNS'),                 # plural nouns
        (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
        (r'.*', 'NN')                     # nouns (default)
     ]
    regexp_tagger = nltk.RegexpTagger(patterns)
    return regexp_tagger

def sents_to_words(sentences):
    tagged_words = []
    for sentence in sentences:
        for word in sentence:
            tagged_words.append(word)
    return tagged_words

def trigram_tag(sentences, default_tagger=get_regexp_tagger()):
    return trigram_tagging.trigram_tag()

