myDictionary = {
    "name": "Konrad",
    "age": "9"
}

get_age = lambda name: myDictionary.get(name)
get_age = lambda name: myDictionary.get(name, 'not found')
print(get_age('name')) # Konrad
print(get_age('not found test ')) # not found



'''
Complete the file_type_getter function. This function accepts a list of tuples, where each tuple contains:

A "file type" (e.g. "code", "document", "image", etc)
A list of associated file extensions (e.g. [".py", ".js"] or [".docx", ".doc"])
The function returns a function for looking up the file type of a given file extension.

Create an empty dictionary to map each file extension to its file type.
Loop through the file_extension_tuples:
Loop through the file extensions.
Add each extension to the dictionary and assign its value to the file type.
For example, if given the following list of tuples:

# list of tuples
[
    ("document", [".doc", ".docx"]),
    ("image", [".jpg", ".png"])
]

# resulting dictionary
{
    ".doc": "document",
    ".docx": "document",
    ".jpg": "image",
    ".png": "image",
}

Return a lambda function that accepts a string (a file extension) and returns its file type from the dictionary.
Use the .get dictionary method in the lambda function to return the file type of the extension if found or "Unknown" if it's missing.
'''

def file_type_getter(file_extension_tuples):
    dict = {}
    
    for tuple in file_extension_tuples:
        for ext in tuple[1]:
            dict[ext] = tuple[0]

    return lambda ext: dict.get(ext, 'Unknown') 
    