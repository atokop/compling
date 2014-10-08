import u4
import utils

# Creates feature set from 300 most common non-stopwords in corpus.
feature_words = u4.top_words_by_frequency(utils.clean(u4.yoursmall_words), 300)
