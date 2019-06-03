import spacy
from nltk.corpus import state_union
from bag_of_words.get_bag_of_words import get_bow
from nltk.corpus import genesis,gutenberg,abc

def main():
    nlp = spacy.load('en')

    # Quick run
    text = genesis.raw("english-kjv.txt")

    # Long run
    # text = ''
    #for file in state_union.fileids():
    #     text += state_union.raw(file)

    word_count = get_bow(text, nlp)
    print("The length of the dictionary is:", len(word_count))

    for i in word_count:
        print(i, end='\n')

main()
