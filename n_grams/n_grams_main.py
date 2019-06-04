import spacy

from nltk.corpus import state_union
from n_grams. ngrams import bigram_text


def main():
    nlp = spacy.load('en')
    text = ''
    for file in state_union.fileids():
        text += state_union.raw(file)
    result_dictionary = bigram_text(text, nlp)
    i = 0
    for occurrences, bigram in result_dictionary.items():
        print(bigram, occurrences)
        i = i +1
        if i > 100:
            break

main()
