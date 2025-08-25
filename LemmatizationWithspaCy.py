import spacy

# Load the spacy English model
nlp = spacy.load("en_core_web_sm")

text2 = "The striped bats are hanging on their feet and ate better"
doc2 = nlp(text2)

for token in doc2:
    print(f"{token.text} -> {token.lemma_}")