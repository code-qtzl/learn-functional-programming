def zipmap(keys, values):
    if not keys or not values:
        return {}  # Base case: If either list is empty, return an empty dictionary

    # Recursive call with the remaining elements
    updated = zipmap(keys[1:], values[1:])

    # Add the first element of keys to the dictionary
    updated[keys[0]] = values[0]


    return updated
