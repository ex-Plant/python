# First example is not correct way of using recursion


def factorial_r(x, curr = 1): 
    print(' x:', x,  ' curr: ', curr,)

    if x <= 1:
        return curr
    curr *= x
    x -= 1
    return factorial_r(x, curr)


res = factorial_r(5)

print('res:', res, )


# solution
def factorial_r(x):
    if x == 0:
        return 1
    return x * factorial_r(x - 1)
