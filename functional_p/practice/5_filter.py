'''
The built-in filter function takes a function and an iterable (in this case a list) and returns an iterator that only contains elements from the original iterable where the result of the function on that item returned True.



In Python:

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(is_even, numbers))
print(evens)
# [2, 4, 6]

Assignment
Complete the remove_invalid_lines function. It accepts a document as input. It should:

Use the built-in filter function and a lambda to return a filtered copy of the input document
Remove any lines that start with a - character.
Keep all other lines and preserve any trailing newlines (\n).
For example, this:

* Star Wars episode 1 is underrated
- Star Wars episode 9 is fine
* Star Wars episode 3 is the best


Should become:

* Star Wars episode 1 is underrated
* Star Wars episode 3 is the best
'''


def remove_invalid_lines(document):
    lines = document.split("\n")
    filtered = filter(lambda line: len(line) == 0 or line[0] != "-", lines  )
    return "\n".join(filtered)

# Solution from boot.dev
def remove_invalid_lines(document):
    return "\n".join(
        filter(lambda line: not line.startswith("-"), document.split("\n"))
    )
