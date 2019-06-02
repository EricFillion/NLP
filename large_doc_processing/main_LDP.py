'''
work in progress. I need to change it so it does one sentence at a time,
rather by characters to avoid sentences getting cut off.
'''

from nltk.corpus import abc
import spacy
def large_doc(text,nlp):
    doc_list = list()
    for i in range(0,len(text)-1000000,1000000):
        temp_text = text[i:i+1000000]
        doc = nlp(temp_text)
        doc_list.append(doc)
    return doc

news = abc.raw("science.txt")

nlp = spacy.load('en')

doc_list = large_doc(news,nlp)


