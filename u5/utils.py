# -*- coding: utf-8 -*-
import nltk
from cPickle import dump, load
from unidecode import unidecode
stopset = set(nltk.corpus.stopwords.words('english'))
f = open("./stopwords.txt", "r")
for line in f.readlines():
    word = line.strip()
    if word not in stopset:
        stopset.add(word)

# Removes stopwords from a list of words.
def remove_stopwords(tagged):
    out = [word for word in tagged if word not in stopset]
    return out

# Cleans out all words with non-alpha characters
def filter_alpha(tagged):
    out = [word for word in tagged if word.isalpha()]
    return out

# Cleans out all words with non-alphanumeric characters.
def filter_alnum(tagged):
    out = [word for word in tagged if word.isalnum()]
    return out

# Removes stopwords, and all non-alpha words
def clean(words):
    return remove_stopwords(filter_alpha(words))

# Removes stopwords, and all non-alpha words
def ascii_clean(words):
    return [unidecode(w) for w in remove_stopwords(filter_alpha(words))]

# Stores an object in a pickle file.
def store(obj, dumpfile="store.pkl"):
    output = open(dumpfile, 'wb')
    dump(obj, output, -1)
    output.close()
    
# Reads an object from a pickle file.
def read(dumpfile="store.pkl"):
    inp = open(dumpfile, 'rb')
    obj = load(inp)
    inp.close()
    return obj

# Gives items of a Frequency Distribution in sorted order.
def sort_freq_dist(freq_dist):
	temp = sorted(freq_dist.items(), key=lambda entry: entry[1])
	temp.reverse()
	return temp

