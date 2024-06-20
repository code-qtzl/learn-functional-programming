def remove_invalid_lines(document):
    # ================================
    #   Approach with defined function
    # ================================
    def good_line(line):
        # excludes the lines that begin with '-' with the 'not' key word
        return not line.startswith('-')

    lines = document.split('\n')
    # using the defined function that checks the condition
    filtered_list = list(filter(good_line, lines))
    clean_list = '\n'.join(filtered_list)

    return clean_list

    # ================================
    #   Approach with lambda function
    # ================================

    # lines = document.split('\n')
    # # Use filter with a lambda function
    # filtered_lines = list(filter(lambda line: not line.startswith('-'), lines))
    # clean_list = '\n'.join(filtered_lines)

    # return clean_list
    


