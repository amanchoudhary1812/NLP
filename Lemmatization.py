import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('omw-1.4')
nltk.download('wordnet')

words = ["running", "ran", "eats", "ate", "better"]

lemmatizer = WordNetLemmatizer()

print("Original Words:", words)
print("Lemmatized (noun):", [lemmatizer.lemmatize(w, pos='n') for w in words])
print("Lemmatized (verb):", [lemmatizer.lemmatize(w, pos='v') for w in words])
print("Lemmatized (adj):", [lemmatizer.lemmatize(w, pos='a') for w in words])