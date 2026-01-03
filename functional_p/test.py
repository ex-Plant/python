import functools
# def add(sum_so_far, x):
#     print(f"{sum_so_far}, x: {x}")
#     return sum_so_far + x

numbers = [1, 2, 3, 4]
sum = functools.reduce(lambda acc, b: acc + b, numbers)

# print(sum)


