from nltk.stem import PorterStemmer

words = ["playing", "played", "plays", "happily", "happiness", "better"]
ps = PorterStemmer()

stems = [ps.stem(word) for word in words]
print("Original Words:", words)
print("Stemmed Words:", stems)
