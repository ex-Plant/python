# At Doc2Doc, we need better internal debugging tools. Complete the args_logger function. It takes a variable number of positional and keyword arguments and prints them to the console.

# Print each positional argument sequentially using numbers and periods as list markers, starting with 1. . For example:
# args_logger("what's", "up", "doc")

# prints to the console:

# 1. what's
# 2. up
# 3. doc

# Sort the keyword argument alphabetically by key with the sorted function.
# Then print the sorted keyword arguments using asterisks (*) as list markers, and with a colon (:) between the key and value. For example:
# args_logger("hi", "there", age=17, date="July 4 1776")

# prints to the console:

# 1. hi
# 2. there
# * age: 17
# * date: July 4 1776

def args_logger(*args, **kwargs):
    kwargs_sorted = sorted(kwargs.keys())

    for index, arg in enumerate(args):
        print(f"{index + 1}. {arg}")

    for kwarg in kwargs_sorted:
        print(f"* {kwarg}: {kwargs[kwarg]}")
    
