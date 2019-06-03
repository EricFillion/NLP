
from text_processing.split_into_sentences import sentence_split

def large_doc(text, nlp):
    text = text.lower()
    sentences = sentence_split(text)
    docs = list()
    doc_text = ''
    for sent in sentences:
        if (len(doc_text)+len(sent)) < 1000000:
            doc_text += sent
        else:
            print("New Doc:", len(doc_text))
            doc = nlp(doc_text)
            docs.append(doc)
            doc_text = sent
    print("Last Doc:", len(doc_text))
    doc = nlp(doc_text)
    docs.append(doc)

    return docs

def docs_to_lemma(docs, nlp):
    new_docs = list()
    for doc in docs:
        doc_list = [token.lemma_ for token in doc]
        doc_string = " ".join(doc_list)
        doc = nlp(doc_string)
        new_docs.append(doc)
    return new_docs

def remove_stop_words(docs, nlp):
    new_docs = list()
    for doc in docs:
        doc_list = [token.text for token in doc if not token.is_stop]
        doc_string = " ".join(doc_list)
        doc = nlp(doc_string)
        new_docs.append(doc)
    return new_docs
