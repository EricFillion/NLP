from collections import Counter, OrderedDict
from text_processing.split_into_sentences import sentence_split
from text_processing.single_doc import doc_stop_words, doc_to_lemma

def bigram(doc):
    # create a list for the result
    result = list()
    # create a list that contains no punctuation
    sentence = list()
    # parse through the document to add all tokens that are words to the sentence list
    for token in doc:
        if token.is_alpha:
            sentence.append(token)
    # parse through the sentence while adding words in groups of two to the result
    for word in range(len(sentence) - 1):
        first_word = sentence[word]
        second_word = sentence[word + 1]
        element = first_word.text + ' ' +  second_word.text
        result.append(element)

    return result

def bigram_text(text, nlp):

    bigrams = list() # list to store occurrence for each bigram
    sentences = sentence_split(text)

    for sent in sentences:
        doc = nlp(sent)
        doc = doc_to_lemma(doc, nlp)
        doc = doc_stop_words(doc, nlp)
        new_result = bigram(doc)
        bigrams.extend(new_result)

    result_counter = Counter(bigrams)

    result_dictionary = OrderedDict(result_counter.most_common())
    return result_dictionary
