valid_formats = [
    "docx",
    "pdf",
    "txt",
    "pptx",
    "ppt",
    "md",
]

# Don't edit above this line


def pair_document_with_format(doc_names, doc_formats):

    #   The zip function combines doc_names and doc_formats into pairs. 
    #   Each element from doc_names is paired with the corresponding element in doc_formats.
    #   list(zip(...)) converts the zip object into a list of tuples.
    zipping = list(zip(doc_names, doc_formats))

#   filter is used to filter out the pairs that do not have a valid format.
#   lambda x: x[1] in valid_formats is a lambda function that checks if the format (the second element of each tuple x[1]) is in the valid_formats list.
#   list(filter(...)) converts the filter object into a list of tuples that pass the filter condition.
    valid_list = list(filter(lambda x: x[1] in valid_formats, zipping))

    return valid_list