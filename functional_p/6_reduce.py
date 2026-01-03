'''
Complete the join and the join_first_sentences functions.

Complete the join function. It's a helper function we'll use in join_first_sentences.
It takes two inputs:
A doc_so_far accumulator string - similar to the sum_so_far variable in the example above.
A sentence string - this is the next string we want to add to the accumulator.
Returns the result of concatenating the "doc" and "sentence" strings together, with a period and a space in between. For example:

doc = "This is the first sentence"
sentence = "This is the second sentence"
print(join(doc, sentence))
# This is the first sentence. This is the second sentence

doc = "This is the first sentence"
sentence = "This is the second sentence"
print(join(doc, sentence))
# This is the first sentence. This is the second sentence

Here's an example of the expected behavior:

joined = join_first_sentences(
    ["This is the first sentence", "This is the second sentence", "This is the third sentence"],
    2
)
print(joined)
# This is the first sentence. This is the second sentence.

'''


import functools
def join(doc_so_far, sentence):
    return doc_so_far + ". " +  sentence

# def join_first_sentences(sentences, n):
#     if n == 0:
#         return ""
#     return functools.reduce(join , sentences[:n]) + "."


def join_first_sentences(sentences, n):
    if n == 0:
        return ""
    return functools.reduce(lambda acc, b: acc + ". " + b , sentences[:n]) + "."
