from __future__ import division
from textutils import *
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import brown
from nltk.corpus import treebank
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import brown, reuters, state_union, words
from nltk.corpus import wordnet

import nltk
import dateutil
import pyparsing
import numpy
import six
import matplotlib
from cPickle import dump, load

def store(obj, dumpfile="store.pkl"):
    output = open(dumpfile, 'wb')
    dump(obj, output, -1)
    output.close()
    
def read(dumpfile="store.pkl"):
    inp = open(dumpfile, 'rb')
    obj = load(inp)
    inp.close()
    return obj

def remove_stopwords_tagged(tagged, stopset):
    out = [(word_with_tag[0], word_with_tag[1]) for word_with_tag in tagged if word_with_tag[0] not in stopset]
    return out

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

def raw_trigram_tag(sentences, default_tagger=get_regexp_tagger(), **kwargs):
    t3 = None
    if "tagger_file" in kwargs.keys():
        t3 = read(kwargs["tagger_file"])
    else:
        tagged_sents = nltk.corpus.brown.tagged_sents() + nltk.corpus.treebank.tagged_sents()
        t0 = default_tagger
        t1 = nltk.UnigramTagger(tagged_sents, backoff=t0)
        t2 = nltk.BigramTagger(tagged_sents, backoff=t1)
        t3 = nltk.TrigramTagger(tagged_sents, backoff=t2)

    if t3:
        store(t3)
    tagged_words = []
    tagged_sentences = []
    for sentence in sentences:
        tagged_sentence = (t3.tag(sentence))
        tagged_sentences.append(tagged_sentence)
        for word in tagged_sentence:
            tagged_words.append(word)
    return (tagged_words, tagged_sentences)

def remove_tags(tag_prefixes, tagged_text):
    out = [(word_with_tag[0]) for word_with_tag in tagged_text for prefix in tag_prefixes  
            if word_with_tag[1].startswith(prefix)]
    return out

def remove_non_english(words):
    out = [(word) for word in words if wordnet.synsets(word)]
    return out

def lemmatize_words(words):
    lemmer = WordNetLemmatizer()
    out = [(lemmer.lemmatize(word)) for word in words if len(lemmer.lemmatize(word)) > 1]
    return out


#Make a stopset
stopset = set(nltk.corpus.stopwords.words('english'))
f = open("./stopwords.txt", "r")
for line in f.readlines():
    word = line.strip()
    if word not in stopset:
        stopset.add(word)

#Read in corpus
corpus_root = '.././Islip13Rain/'
classevent_wordlists = PlaintextCorpusReader(corpus_root, '.*') 

#sent tokenize
sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

# CEsents = sent_tokenizer.tokenize(classevent_wordlists.raw())
CEsents = classevent_wordlists.sents()

#tag and filter
def trigram_tag(sentences, default_tagger=get_regexp_tagger(), **kwargs):
    tagged_words = raw_trigram_tag(sentences)
    tagged_words = remove_stopwords_tagged(tagged_words, stopset)
    pos_filtered = remove_tags(["NN", "VB"], tagged_words)
    pos_filtered = remove_non_english(pos_filtered)
    pos_filtered = [(word.lower()) for word in pos_filtered]
    pos_filtered = lemmatize_words(pos_filtered)
    set_pos_filtered = list(set(pos_filtered))
    set_pos_filtered = sorted(set_pos_filtered, key=lambda word: pos_filtered.count(word))
    return set_pos_filtered

