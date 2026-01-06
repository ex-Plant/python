# Complete the doc_format_checker_and_converter function.

# It takes a conversion_function and a list of valid_formats as parameters. It should return a new function that takes two parameters of its own:

# filename: The name of the file to be converted
# content: The content (body text) of the file to be converted
# If the file extension of the filename is in the valid_formats list, then it should return the result of calling the conversion_function on the content.
# Otherwise, it should raise a ValueError with the message invalid file format.

def doc_format_checker_and_converter(conversion_function, valid_formats):
    def foo(filename, content):
        ext = filename.split('.')
        if ext[1] in valid_formats:
            return conversion_function(content)
        raise ValueError('invalid file format')

    return foo



# Don't edit below this line


def capitalize_content(content):
    return content.upper()


def reverse_content(content):
    return content[::-1]
