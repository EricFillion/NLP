
from text_processing.large_doc import large_doc, docs_to_lemma, remove_stop_words

def get_bow(text, nlp):

    docs = large_doc(text, nlp)
    word_count = {}  #dictionary for the bag of words
    docs = remove_stop_words(docs, nlp)
    docs = docs_to_lemma(docs, nlp)

    for doc in docs:
        for token in doc:
            if token.is_alpha:
                if token.text not in word_count.keys():
                    word_count[token.text] = 1
                else:
                    word_count[token.text] += 1

    #Sort word_count by highest occurrence to lowest occurrence
    word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    return word_count
