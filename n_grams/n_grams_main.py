import spacy
from ngrams import bigram

# load English model
nlp = spacy.load('en')

# create a document
doc = nlp("I ordered steak from the butcher.")

result = bigram(doc)

#print("result type: ",type(result))

for element in result:
    #print("element type: ",type(element))
    for token in element:
        print(token, end=' ')
        #print("token type: ", type(token))
    print() #new line