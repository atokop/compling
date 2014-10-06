# -*- coding: utf-8 -*-
import nltk
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
def filter_alpha(tagged):
    out = [word for word in tagged if word.isalnum()]
    return out

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
