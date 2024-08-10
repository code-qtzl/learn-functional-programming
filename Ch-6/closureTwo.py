def new_collection(initial_docs):

    # Create a copy of initial_docs to avoid modifying the original list
    list_items = initial_docs.copy()

    def close_copy(new_doc):
        # Append the new document to the copied list
        list_items.append(new_doc)
        # Return the updated list
        return list_items.copy()

    return close_copy