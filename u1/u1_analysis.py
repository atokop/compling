def most_frequent(text):
    return FreqDist(ClassEvent).items()[:20]

def most_frequent_above_n(text, n):
    return FreqDist([w for w in ClassEvent if len(w) > n]).items()[:20]
