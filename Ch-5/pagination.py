from functools import reduce

def paginator(page_length):
    def paginate(document):
        # Split the document into individual words
        words = document.split()
        def add_word_to_pages(pages, word):

            # If pages list is empty, initialize it with the first word
            if not pages:
                return [word]
            
            # Get the current page (last page in the list)
            current_page = pages[-1]

            # Check if adding the new word to the current page exceeds the page length
            if len(current_page) + len(word) + 1 > page_length:
                # If it does, start a new page with the new word
                pages.append(word)
            else:
                # If it doesn't, add the word to the current page
                pages[-1] = current_page + ' ' + word
            return pages
        
        # Use reduce to iterate over the words and build the list of pages
        return reduce(add_word_to_pages, words, [])

    return paginate
