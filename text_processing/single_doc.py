def doc_to_lemma(doc, nlp):
    doc_list = list()
    for token in doc:
        if token.lemma_ != '-PRON-':
            doc_list.append(token.lemma_)
        else:
            doc_list.append(token.lower_)

    doc_string = " ".join(doc_list)
    doc = nlp(doc_string)

    return doc


def doc_stop_words(doc, nlp):
    doc_list = [token.text for token in doc if not token.is_stop]
    doc_string = " ".join(doc_list)
    doc = nlp(doc_string)
    return doc






