def remove_emphasis_from_word(word):
    return word.replace('*', '').replace('**', '')


def remove_emphasis_from_line(line):
    return line.replace('*', '').replace('**', '')

def remove_emphasis(doc_content):
    # Applies a lambda function to each item in doc_content
    new_content = map(lambda item: 
                            # Applies remove_emphasis_from_line if item is a string
                           remove_emphasis_from_line(item) 
                           if isinstance(item, str) 
                            # Applies remove_emphasis_from_word to each word if item is a list
                            else list(map(remove_emphasis_from_word, item)) 
                           if isinstance(item, list) 
                            # Return the item unchanged if it's neither a string nor a list
                            else item, doc_content)
    # Join the new_content into a single string
    new_doc = ''.join(new_content)

    return new_doc