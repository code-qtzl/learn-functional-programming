def change_bullet_style(document):
    # Easiest way to do this challenge.
    # change = document.replace('-', '*')
    # return change
    # ======================================

    # Parameter:
    # document (str): The input document as a string.

    # splitting doc into list of lines
    lines = document.split('\n')
    # passes convert_line function to each line of the input string
    changed_lines = map(convert_line, lines)
    # joins the modified lines back together
    result = '\n'.join(changed_lines)
    return result
    


# Don't edit below this line

def convert_line(line):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line