
def args_logger(*args, **kwargs):
    formatted_args = [f"{i+1}. {arg}\n" for i, arg in enumerate(args)]
    
    # Print formatted arguments and any keyword arguments
    # print(f"{', '.join(formatted_args)} {kwargs}")

    # Sort keyword arguments by key and format with asterisks and colons
    sorted_kwargs = sorted(kwargs.items())
    formatted_kwargs = [f"* {key}: {value}\n" for key, value in sorted_kwargs]
    
    # Print formatted positional arguments and formatted keyword arguments
    print(f"{''.join(formatted_args)}{''.join(formatted_kwargs)}")


args_logger("what's", "up", "doc")
args_logger("hi", "there", age=17, date="July 4 1776")