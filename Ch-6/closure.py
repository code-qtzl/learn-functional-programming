def word_count_aggregator():
    total_count = 0
    def words_input(doc = ''):
        # Use 'nonlocal' to indicate that we want to modify the 'total_count' variable from the enclosing scope
        nonlocal total_count
        # Split the input string 'doc' into a list of words
        word_list = doc.split()
        # Count the number of words in the current 'doc'
        count = len(word_list)
        # Add the count of the current words to the total word count
        total_count += count

        return total_count
        
    return words_input