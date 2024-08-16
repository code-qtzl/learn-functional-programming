def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        
        # Convert positional arguments
        # Use a generator expression to filter out only string arguments
        # Apply convert_md_to_txt to each string argument
        # Convert the map result to a list
        new_args = list(map(convert_md_to_txt, (arg for arg in args if isinstance(arg, str))))
        
        # Convert keyword arguments
        # Use kwargs.items() to get an iterable of (key, value) tuples
        # Apply convert_md_to_txt to each value using a lambda function
        # Convert the map result to a dictionary
        new_kwargs = dict(map(lambda kv: (kv[0], convert_md_to_txt(kv[1])), kwargs.items()))
        
        # Call the decorated function with the new arguments
        # Use * to unpack new_args and ** to unpack new_kwargs
        return func(*new_args, **new_kwargs)

    return wrapper


# don't touch below this line


def convert_md_to_txt(doc):
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")
    return "\n".join(lines)
