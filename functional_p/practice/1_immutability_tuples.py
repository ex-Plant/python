def add_prefix(document, documents):
    prefix = f"{len(documents)}. "
    new_doc = (prefix + document,)
    documents += new_doc
    return documents
