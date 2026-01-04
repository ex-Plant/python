import functools
number = [1, 2, 3, 4 ]
total = functools.reduce(lambda a, b: a + b, number)
print(total)

