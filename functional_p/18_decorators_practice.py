# Complete the markdown_to_text_decorator function. It can decorate a function with any number of string arguments, no matter if they're positional or keyword args. It will run the decorated function, but first strip out any Markdown heading symbols (see below for an explanation of Markdown headings).

# It should return a wrapper function that takes *args and **kwargs. The wrapper should:

# Map the *args to a new list where each string is converted to plain text using convert_md_to_txt.
# Map the **kwargs to a new dictionary where each "value" is converted to plain text using convert_md_to_txt. The "key" should remain the same.
# Use the .items() dictionary method to pass a list of tuples of key-value pairs to map
# Create a function for map which changes the value of an item tuple with convert_md_to_txt
# Return the result of calling the decorated function with the new arguments.

def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        stripped_args = list(map(convert_md_to_txt, args))
        
        # Without lambda
        def strip_tuple(item):
            return  [item[0], convert_md_to_txt(item[1])]
        newD = dict(map(strip_tuple , kwargs.items()))

        # newD = dict(map(lambda item: [item[0], convert_md_to_txt(item[1])] ,kwargs.items()))        
        return func(*stripped_args, **newD)
    return wrapper



def convert_md_to_txt(doc):
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")
    return "\n".join(lines)



@markdown_to_text_decorator
def concat(first_doc, second_doc):
    return f"""  First: {first_doc}
  Second: {second_doc}"""


@markdown_to_text_decorator
def format_as_essay(title, body, conclusion):
    return f"""  Title: {title}
  Body: {body}
  Conclusion: {conclusion}"""
