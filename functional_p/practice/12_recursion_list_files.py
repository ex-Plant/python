# Steps
# Create an empty list to store the file paths.
# Use a for-loop to iterate through the keys of the parent_directory dictionary:
# Use the key to create a new file path by concatenating a slash / and the key to the end of the current_filepath.
# If the value is None, the key is a filename. .append() the new file path to the list of file paths.
# Otherwise, the value is a child directory dictionary. Recursively call list_files with the child directory dictionary and the new file path.
# Use .extend() to add the results of the recursive call to the list of file paths.
# Return the list of file paths.

# From:
{
    "Documents": {
        "Proposal.docx": None,
        "Receipts": {
            "January": {
                "receipt1.txt": None,
                "receipt2.txt": None
            },
            "February": {
                "receipt3.txt": None
            }
        }
    },
}

# to:

[
    "/Documents/Proposal.docx",
    "/Documents/Receipts/January/receipt1.txt",
    "/Documents/Receipts/January/receipt2.txt",
    "/Documents/Receipts/February/receipt3.txt"
]

def list_files(parent_directory, current_filepath=""):
    filenames = []

    for key in parent_directory:
        curr = current_filepath + "/" + key 
        if parent_directory[key] is None:
            filenames.append(curr)
        else:
            res = list_files(parent_directory[key], curr)
            filenames.extend(res)
    return filenames


# Without extend 

def list_files2(parent_directory, current_filepath=""):
    filenames = []

    for key in parent_directory:
        curr = current_filepath + "/" + key 
        if parent_directory[key] is None:
            filenames.append(curr)
        else:
            filenames += list_files(parent_directory[key], curr)
    return filenames