def get_common_formats(formats1: list, formats2: list) -> set:

    # ============================================================
    # Returns the intersection of two lists of strings as a set.
    
    # Parameters:
    # list1 (list): The first list of strings.
    # list2 (list): The second list of strings.
    
    # Returns:
    # set: A set containing the intersection of the two lists.
    # ============================================================
    # Convert lists to sets
    set1 = set(formats1)
    set2 = set(formats2)

    # Find intersection
    result =  set1.intersection(set2)

    return result