import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('punkt_tab') 

import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

text = "Artificial Intelligence is transforming the world. NLP is a key part of AI. Machines are learning to understand human language."

# ---------- Task 1: Sentence Tokenization ----------

# Using NLTK
from nltk.tokenize import sent_tokenize
nltk_sentences = sent_tokenize(text)
print("NLTK Sentence Tokenization:", nltk_sentences)

# Using spaCy
doc = nlp(text)
spacy_sentences = [sent.text for sent in doc.sents]
print("spaCy Sentence Tokenization:", spacy_sentences)

# Compare outputs
print("Are both same?", nltk_sentences == spacy_sentences)

# ---------- Task 2: Word Tokenization ----------

# Using NLTK
from nltk.tokenize import word_tokenize
nltk_words = word_tokenize(text)
print("\nNLTK Word Tokens:", nltk_words)

# Using spaCy
spacy_words = [token.text for token in doc]
print("spaCy Word Tokens:", spacy_words)

# Count unique tokens
unique_tokens = set(nltk_words)
print("Number of Unique Tokens:", len(unique_tokens), "\nUnique Tokens:", unique_tokens)