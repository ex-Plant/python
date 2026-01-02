def square(x):
    return x * x

nums = [1, 2, 3, 4]
squared_nums = map(square, nums)
print(list(squared_nums))
