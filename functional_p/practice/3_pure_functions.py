'''
Complete the pure_add function. It should take two numbers as input and return their sum.
This function should be pure - it should always return the same result given the same inputs,
and should not cause any side effects.

Remember: pure functions should not:
- Modify global variables
- Print to console
- Read from files/network
- Depend on random numbers or current time
- Modify their input parameters

Example:
pure_add(2, 3) should always return 5
pure_add(2, 3) should always return 5 (same inputs, same output)
'''

def pure_add(x, y):
    return x + y

# Test the function
print("Testing pure_add:")
print(f"pure_add(2, 3) = {pure_add(2, 3)}")
print(f"pure_add(5, 7) = {pure_add(5, 7)}")
print(f"pure_add(0, 0) = {pure_add(0, 0)}")

# Compare with an impure version
total = 0
def impure_add(x):
    global total
    total = total + x
    return total

print("\nTesting impure_add:")
print(f"impure_add(2) = {impure_add(2)}")  # First call: 2
print(f"impure_add(3) = {impure_add(3)}")  # Second call: 5 (different result!)
print(f"impure_add(2) = {impure_add(2)}")  # Third call: 7 (same input, different output!)
