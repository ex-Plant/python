def word_count_aggregator():
    count = 0
    def foo(doc):
        nonlocal count
        count += len(doc.split())
        return count
    return foo
         

    
