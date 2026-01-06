def foo_countdown(x):
    if x ==0:
        return 
    print(x)
    foo_countdown(x-1) 
foo_countdown(10)