import spacy
from bag_of_words.get_BOW import get_bow
from nltk.corpus import state_union

def main():
    nlp = spacy.load('en')


    text = ''
    for file in state_union.fileids():
          text += state_union.raw(file)

    word_count = get_bow(text, nlp)
    print("The length of the dictionary is:", len(word_count))

    for i in word_count:
        print(i, end='\n')

main()
