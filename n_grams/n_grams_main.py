import spacy
from ngrams import bigram

# load English model
nlp = spacy.load('en')

# create a document
doc = nlp("I ordered steak from the butcher.")

result = bigram(doc)

for element in result:
    for token in element:
        print(token, end=' ')
    print() #new line