def find_longest_word(content, longest=""):
    if isinstance(content, str):
        words = content.split()
        if words:
            first_word = words[0]
            rest_of_words = words[1:]
            
            if len(first_word) > len(longest):
                longest = first_word
            
            # Recursively call with the remaining words
            return find_longest_word(rest_of_words, longest)

    elif isinstance(content, list):
        if len(content) == 0:
            return longest
        
        first_element = content[0]
        rest_of_content = content[1:]
        
        # Recursively call with the first element and update longest
        longest = find_longest_word(first_element, longest)
        
        # Continue with the rest of the list
        return find_longest_word(rest_of_content, longest)

    return longest