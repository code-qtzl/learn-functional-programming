def doc_format_checker_and_converter(conversion_function, valid_formats):
    def new_func(filename, content):
        file_parts = filename.split('.')

        if len(file_parts) > 1:
            file_extension = file_parts[-1]
        
        if file_extension in valid_formats:
            return conversion_function(content)
        else:
            raise ValueError('Invalid file format')

    return new_func


def capitalize_content(content):
    return content.upper()


def reverse_content(content):
    return content[::-1]
