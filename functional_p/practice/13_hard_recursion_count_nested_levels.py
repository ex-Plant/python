# Complete the count_nested_levels function. It takes a dictionary of nested documents, the target document id and the current level of the document.

# Loop over document_ids in the nested_documents dictionary
# If the current document_id matches the target_document_id, return its level of nesting
# If the target_document_id is not found, recursively call count_nested_levels on the current document_id and increment the level
# If the recursive call found the target_document_id's level, return it
# If the target_document_id doesn't exist, the function should return -1
# Example
# In this dictionary, the document with id 3 is nested 2 levels deep. Document 2 is nested 1 level deep.

# {
#     1: {
#         3: {}
#     },
#     2: {}
# }



def count_nested_levels(nested_documents, target_document_id, level=1):
    for document_id in nested_documents:
        if document_id == target_document_id:
            return level
            
        found_level = count_nested_levels(
            nested_documents[document_id], target_document_id, level + 1
        )
        if found_level != -1:
            return found_level
    return -1
