import functools

def join(doc_so_far, sentence):
    # print(f"doc: {doc_so_far}, sentence: {sentence}")
    if doc_so_far:
        doc_so_far += ". "
    return doc_so_far + sentence
    

def join_first_sentences(sentences, n):
    # getting the first n sentence
    first_n_sentences = sentences[:n]

    # condition returns empty if there are no items
    if not first_n_sentences:
        return ""

    # functools.reduce is joining the sentences
    result = functools.reduce(join, first_n_sentences)

    return result + "." + ""