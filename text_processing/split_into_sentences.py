
def sentence_split(text):
    sentences = list()
    sent = ''
    for char in text:
        sent += char
        if char in ('.', '?', '!'):
            sentences.append(sent)
            sent = ''
    return sentences
