def sum_nested_list(lst):
    total_size = 0 # keeping track of the size
    for item in lst:
        if isinstance(item, int): # If the item is an integer, add it to the total size
            total_size += item # Add integer directly to total_size
        elif isinstance(item, list):
            total_size += sum_nested_list(item) # Recursively add size of nested list

    return total_size

    