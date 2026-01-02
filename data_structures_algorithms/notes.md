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

# Exponents - `wykładnik potęgowy`

Mathematical operator that multiplies a number by itself a certain amount of times.

```py
square = 2 ** 3

# sześcian
cube = 2 ** 3
```

Sometimes exponents are also written using (^) symbol  
5^2 = 25 (Five to the power of 2) `5 do potęgi 2`  
Five is a 'base' - `baza`
Two is the `exponent - wykładnik`

Exponents grow very large very quickly
Super important to understand how it affects the speed of execution of an algorithm. It the number of operations grows quickly as the amount if input data increase - the algorithm will be slower and slower.

An example of exponential grow is `geometric progression - ciąg geometryczny`

Each term is found by multiplying previous term by a fixed number.
For example number of employees doubles each year.

```text
    total = a1 x r^n
```

a1 = number of employees
r = 2 (because it doubles)
n = number of years

Let's say we start with 10 employees
After 4 years we would have

```text
10 * 2 * 2 * 2 = 160
total = 10 * 2**4
2**4 = 16
10* 16 = 160
```

💡 Example

```py
def get_follower_prediction(follower_count, influencer_type, num_months):
    def multiply(val):
        return follower_count * val ** num_months

    if influencer_type == "fitness":
        return multiply(4)

    if influencer_type == "cosmetic":
        return multiply(3)

    return multiply(2)

```

# Linear growth - `wzrost liniowy` O(n)

`Linear` growth meands that number of operations within an algorithm grows steadily as the input data grow. The function performs exactly one pass through the input list:

- Input size: n elements in nums
- Operations: n iterations, each doing O(1) work
- Total time: O(n) - linear growth with input size

```py
def summed(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum
```

# Non-linear growth

Example of non linear growth is a `quadratic growth O(n^2)` - wzrost kwadratowy.

For example nested loop whee each loop depends on input size

```py
def does_name_exist(first_names, last_names, full_name):
    for name in first_names:
        for last_name in last_names:
            if f"{name} {last_name}" == full_name:
                return True
    return False
```

Obviously we should try to write code that is not causing usage of resources to grow quadraticaly. Otherwise this will affect

- CPU - a lot of computation (slow execution)
- RAM - eating memory
- disk space

❗️ The only exception is security and cryptography - we want to force attackers to waste resources.

# Logarithms - `logarytmy`

Inverse of an exponent

`What is the power that we need to raise the number to get the result`

```text
2^4 = 16
log2(16) = 4
Because 2**4 = 16

log10(1000) = 3
Because 10**3 = 1000
```

We read it:  
Log base 2 of 16 -
`Logarytm o podstawie dwa z szesnastu` lub `log 2 z 16`

```py
import math
def get_influencer_score(num_followers, average_engagement_percentage):
    return average_engagement_percentage * (math.log(num_followers, 2))
```

❗️ Exponents grow very quickly and logarithims grow extremely slowly!  
2\*\*20 = 1,048,576  
log2(1,048576) = 20

Because they grow so slow they are super useful in coding and cs.  
`If execution of our program grows logarithmically it means it is gonna be very fast.`

✅ It's nice if we can write code that uses `log(n)` time to run where `n` is an amount of data to process
log(n) time

For example, let's say we have a list of 1,000,000 users, and we want to write an algorithm that finds the user with the most followers.  
If it takes 1 millisecond to check one user (let's just pretend), a linear algorithm would take 1,000,000 milliseconds, or about 16 minutes and 40 seconds.  
A quadratic algorithm (exponent) would take 1,000,000,000,000 milliseconds, or about 31.7 years.  
However, a logarithmic algorithm would only take 20 milliseconds!

# Factorials - `silnia`

The factorial of a positive integer n, written n!, is the product of all positive integers less than and equal to n.

```text
5! = 5 * 4 * 3 * 2 * 1 = 120
```

`The results of a factorial grow even faster than exponentiation!`

```py
def num_possible_orders(num_posts):
    res = 1
    for n in range(0, num_posts):
        res *= n + 1
    return res

```

❗️Factorials are useful whenever you're trying to `count how many ways a collection can be ordered`. For example, how many different ways can a deck of cards be arranged?

The first card could be any of the 52 cards.  
The second card can be any of the 51 remaining cards.  
The third card can be any of the 50 remaining cards, and so on.

That means the total number of possibilities is the 52 options multiplied by 51 options multiplied then by 50 options, and so on.

```text
52 * 51 * 50 ... * 2 * 1
```

# Logarithmic Scale

In some cases, data can span several orders of magnitude, making it difficult to visualize on a linear scale. A logarithmic scale can help by compressing the data so that it's easier to understand.
The Trade-off

```py
def log_scale(data, base):
    list = []
    for value in data:
        list.append(math.log(value, base))
    return list
```

1. Linear Scale: Precise for Addition/Subtraction.

   - Example: "How many more followers does Person A have than Person B?"

2. Logarithmic Scale: Precise for Multiplication/Division.
   - Example: "How many times larger is Person A's audience than Person B's?"

As a developer, if you use a linear scale for follower counts ranging from 1 to 1B, you are creating a useless representation. You lose all precision for the bottom 90% of your users. They all become "zero" visually.

The log scale doesn't "lie" about the data; it changes the focus to orders of magnitude. In the influencer industry, moving from 1,000 to 10,000 followers is a "precise" Tier change. A log scale captures these Tiers accurately.

# Big O Notation - `notacja dużego O`

(Order n)

`Big O analysis` is used to `compare algorithms` by classyfing their `time complexity`.

When comparing them we always take into account worst case growth rate.
We write like the following:

```text
0(formula)
```

Formula describes how run time or space requirements grows as the input size grows:

- O(1) - constant `złożoność stała`
- O(log n) - logarithmic - `złożoność logarytmiczna`
- O(n) - linear - linearna
- O(n log n) - linearithmic
- O(n^2) - squared
- O(n^3) - cubic
- O(2^n) - exponential
- O(n!) - factorial `złożoność silniowa`

As the input size grows algorithms becomes slower to complete - `the rate at wich they become slower` is defined by their Big O category

| Input size (n) | O(1) | O(log₂ n) | O(n) | O(n log₂ n) | O(n²) | O(n³) | O(2^n) | O(n!)   |
| -------------- | ---- | --------- | ---- | ----------- | ----- | ----- | ------ | ------- |
| n=1            | 1    | 0         | 1    | 0           | 1     | 1     | 2      | 1       |
| n=2            | 1    | 1         | 2    | 2           | 4     | 8     | 4      | 2       |
| n=4            | 1    | 2         | 4    | 8           | 16    | 64    | 16     | 24      |
| n=8            | 1    | 3         | 8    | 24          | 64    | 512   | 256    | 40320   |
| n=10           | 1    | 3         | 10   | 33          | 100   | 1000  | 1024   | 3628800 |
| n=16           | 1    | 4         | 16   | 64          | 256   | 4096  | 65536  | 2.09e13 |
| n=20           | 1    | 4         | 20   | 86          | 400   | 8000  | 1.05e6 | 2.43e18 |
| n=32           | 1    | 5         | 32   | 160         | 1024  | 32768 | 4.29e9 | 2.63e36 |

💡 Scientific notation  
e13 means: multiply by 10¹³ (10 to the power of 13)  
2.09 * 10^13 = 20,900,000,000,000 (13 numbers in total after .)
See chart:  
https://cdn-media-1.freecodecamp.org/images/1*KfZYFUT2OKfjekJlCeYvuQ.jpeg

# O(nm)

Similar to O(n^2) but with two inputs affecting time complexity of an algorithm  
If n and m increase in the same rate then O(nm) is effectively the same as O(n^2), otherwise we have to track complexity separately.

```py
all_handles = [
    ["cosmofan1010", "cosmogirl", "billjane321"],
    ["cosmokiller", "gr8", "cosmojane3"],
    ["iloveboots", "paperthin"]
]
brand_name = "cosmo"

def get_avg_brand_followers(all_handles, brand_name):
    name_occurances = 0
    for user_handles in all_handles:
        for handle in user_handles:
            if (brand_name in handle):
                name_occurances += 1
    return  name_occurances / len(all_handles)

```

Regarding Big O, the number of influencers (the number of lists) matters. That's our n. However, the average number of followers of each influencer (the average length of the lists) is just as important. That's our m.

# Big O Analysis

Is a theoretical tool that is not used to calculate actual runtime of an algorithm. We are not using it to get the exact vals of how will it take to finish this or that. We only care about the proportional change, the `theoretical growth rate`.

So the following is O(n)

```py
def print_names_once(names):
    for name in names:
        print(name)
```

And this also O(n) even though in theory we could write it O(2 times n)

```py
def print_names_twice(names):
    for name in names:
        print(name)
    for name in names:
        print(name)

```

In Big O analysis we drop all constants because while they affect the runtime, they don't affect the change in the runtime.

# O(1) - Order one - `Duże O jeden`

No matter the size of input, time complexity stays the same
For example in python we can search an item within dictionary by it's key, and no matter the size it will always stay the same.

`Dictionary lookups are O(1) ` - extremely efficient and a very good reason to choose dictionary as a data structure.

💡 JavaScript objects also have O(1) average-case lookup time for property access.

```js
const obj = { name: "John", age: 30 };
console.log(obj.name); // O(1) - hash table lookup
```
