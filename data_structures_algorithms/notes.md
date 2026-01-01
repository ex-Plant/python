# Data Structeres

Are just `organizational tools` that allow more advanced algorithms.

The simplest data structeres includes:

- `lists: ordered collections of data`
- `dictionaries: key value mappings`
- `sets: unordered collections of unique data`

# Algorithm

Is an unambigiuos `instruction` of how to achieve some result, `solve a problem` usually written in pseudocode
In computer science algorithms are:

- `defined`: a specific sequence of steps
- `unambigious`: there is a correct interpretation of steps
- `implementable` - can be exectued using software and hardware

Example of super simple algorithm

```python
def find_minimum(nums):
    min = float("inf")
    if len(nums) == 0:
        return None
    for num in nums:
        if num < min:
            min = num
    return num

print(find_minimum([1, 2, 3, 4]))
```

# Exponents

`Wykładnik potęgowy`
Mathematical operator that multiplies a number by itself a certain amount of times.

```py
square = 2 ** 3

# sześcian
cube = 2 ** 3
```

Sometimes exponents are also written using (^) symbol  
5^2 = 25 (Five to the power of 2)  
Five is a 'base'  
Two is the `exponent`

Exponents grow very large very quickly
