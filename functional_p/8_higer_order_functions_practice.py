# Complete the restore_documents function in one line - if you can. It takes two tuples of document strings, originals and backups, as input and returns a set.

# Convert all documents to the same case with .upper() for comparison.
# Filter out documents that are corrupted strings of random numbers with .isdigit().
# Return a set that combines (and deduplicates) the documents from originals and backups.

def restore_documents(originals, backups):
    return set(filter(lambda x: x.isdigit() == False, map(lambda x: x.upper(), originals + backups)))


# Solution
def restore_documents_solution(originals, backups):
    return set(
        filter(
            lambda doc: not doc.isdigit(),
            map(lambda doc: doc.upper(), originals + backups),
        )
    )
