def word_count_memo(document, memos):
    memo_copy = memos.copy()
    
    if document in memo_copy:
        return memo_copy[document], memo_copy

    count = word_count(document)
    
    # Store the word count in memo_copy
    memo_copy[document] = count 
    
    return count, memo_copy

# Don't edit below this line


def word_count(document):
    count = len(document.split())
    return count
