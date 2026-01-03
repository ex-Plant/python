total = 0
def dirty_add(x):
    total = total + x

    return total
    # different result every time


print(dirty_add(10))
print(dirty_add(10))
print(dirty_add(10))
