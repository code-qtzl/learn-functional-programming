def find_longest_word(content, longest=""):
    # Check if content is empty (None, empty list, or empty string)
    if not content:
        return longest
    
    # If content is a string
    if isinstance(content, str):
        # Split the string into a list of words
        words = content.split()
        # Proceed if there are words in the list
        if words:
            # Take the first word and the rest of the words
            first_word = words[0]
            rest_of_words = words[1:]
            
            # If the first word is longer than the current longest, update longest
            if len(first_word) > len(longest):
                longest = first_word
            
            # Recursively call the function with the remaining words and updated longest
            return find_longest_word(rest_of_words, longest)
    
    # If content is a list
    elif isinstance(content, list):
        # If the list is empty, return the current longest
        if len(content) == 0:
            return longest
        
        # Take the first element of the list and the rest of the list
        first_element = content[0]
        rest_of_content = content[1:]
        
        # Recursively call the function with the first element and the current longest
        # Update longest with the result from processing the first element
        longest = find_longest_word(first_element, longest)
        
        # Recursively call the function with the rest of the list and the updated longest
        return find_longest_word(rest_of_content, longest)
    
    # If content is neither a string nor a list, return the current longest
    return longest