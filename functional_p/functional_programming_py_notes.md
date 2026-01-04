# Imperative (procedural) programming

We need to declare both what we want to happen and how we want it to happen.

Imperative:

```py
car = create_car()
car.add_gas(10)
car.clean_windows()
```

# Declarative programming

Focus on `what` we want to happen not `how` it should happen.

Functional programming is all about `creating functions instead of mutating state`.

`Main purpose of functional programming is to make our code more declarative.`

Great example of declarative programming is css
We don't care about all the steps, we just want to change the color of each button on the page.

```css
button {
  color: red;
}
```

Hiding implementation on the low level is declarative programming.

This is an example of imperative programming where we define each step.

```py
def get_average(nums):
    total = 0
    for num in nums:
        total += num
    return total / len(nums)
```

And with declarative approach:

```py
def get_average(nums):
    return sum(nums) / len(nums)
```

We do not keep track of the state (total), we only care about the result.

````py
return clean_windows(add_gas(create_car()))
``

We never change the car variable, we are creating new values (immutability).

# Functional programming basic concepts

- higher order functions
- first class functions
- pure functions
- recursion
- closures
- currying

# Immutability

Once the val is created it never changes.
Immutable data is easier to think about and work with. When 10 different functions have access to the same variable, and you're debugging a problem with that variable, you have to consider the possibility that any of those functions could have changed the value.

When a variable is immutable, you can be sure that it hasn't changed since it was created. It's a helluva lot easier to work with.

Generally speaking, `immutability means fewer bugs and more maintainable code.`

# Tuples vs Lists

Both ordered sets of vals but
`tuples are immutable` - you can not append to a tuple. You can create a new copy of a tuple with added value.

```py
ages = (16, 21, 30)
more_ages = (80,) # note the comma! It's required for a single-element tuple
# 'all_ages' is a brand new tuple
all_ages = ages + more_ages
# (16, 21, 30, 80)

# or we can even reassign the same variable to point to a new tuple:
ages = ages + more_ages
# (16, 21, 30, 80)
````

# sorted()

Sort items in the list

```py
def get_median_font_size(font_sizes):
    length = len(font_sizes)
    if length == 0 :
        return None
    sorted_sizes = sorted(font_sizes)
    if length % 2 == 0:
        return sorted_sizes[length // 2 - 1 ]
    return sorted_sizes[length // 2]
```

# Classes vs functions

Functional programming and object-oriented programming are styles for writing code.
Of the four pillars of OOP (inheritance, polymorphism, abstraction encapsulation), inheritance is the only one that doesn't fit with functional programming.

Default to functions. If we need something stateful and long-lived we might reach for classes.

Classes encourage you to think about the world as a hierarchical collection of objects. Objects bundle behavior, data, and state together

Functions encourage you to think about the world as a series of data transformations. Functions take data as input and return a transformed output.

# strip() #replace() #upper()

Equicalent of trim

variations:

- lstrip() - trims left hand side
- rstrip() - trims right hand side

```py
def format_line(line):
    stripped = line.strip()
    capitalized = stripped.upper()
    removedPeriods = capitalized.replace('.', '')
    appended = f"{removedPeriods}..."
    return appended
    # return f"{line.rstrip().capitalize().replace(',', '')}...."
```

# Statements vs Expressions

`Statements - actions to be carried out.`  
"Set n to 7"  
"Define a function named greet"  
"If x > 10, print a greeting to Alice"

```py
n = 7  # Variable assignment statement

def greet(name):  # Function definition statement
    return f"Hello, {name}!"

if x > 10:  # `if` statement
    print(greet("Alice"))

for i in range(n):  # `for` loop statement
    print(i)
```

Expressions are a `subset of statements that produce values`.  
Every function call is an expression!  
Even if a Python function doesn't have a return statement, it still implicitly returns None.

```py
result = 2 + 2  # Arithmetic expression
length = len("hello")  # Function call expression
total_cost = len(items) * cost  # Multiple expressions combined into one
```

Because expressions produce values they are reusable and declarative.
In functional programmin we should aim to use expressions over statements.
Expression:

```py
return sum([1, 2, 3])
```

We could do that in a series of steps but we would have to combine expressions:

```py
total = 0
for n in [1, 2, 3, 4]:
    total += n
```

`Expressions are reusable, declarative, do not mutate values and minize side effects`

# Ternary expression

We can change

```py
result = 0
if number % 2 ==0:
    result = number  / 2
else:
    result = (numer * 3 ) + 1
```

To a ternary expression and avoid mutating state!

```py
result = number / 2 if number % 2 == 0 else (number * 3) + 1
```

Like in js we should not overuse it as they tend to be hard to read

# First Class functions

`First class functions` means that a function in python can be treated like any other object

- assigned to a value (functions as values)
- passed as arguments to other functions
- returned from a function
- stored in a data structure

In python functions are just values, so we can assign a function to a variable

```py
def foo(a, b:
    return a + b

sum_foo = foo
print(sum_foo(2, 2)) # 4
```

# Anonymous functions - lambda

In python unnamed functions are called `lambda `
Example of a functions that takes `x` as an argument and returns `x + 1`

```py
lambda x: x + 1
```

We can assing it to a variable

```py
addone = lambda x: x + 1
```

It is equivalent of:

```js
const addOne = (x) => x + 1;
```

Like in js result of a function expression is returned automaticaly.

```py
myDictionary = {
    "name": "Konrad",
    "age": "9"
}

get_age = lambda name: myDictionary.get(name)
get_age = lambda name: myDictionary.get(name, 'not found')
print(get_age('name')) # Konrad
print(get_age('not found test ')) # not found
```

Example of function returned from another function

```py
def file_type_getter(file_extension_tuples):
    file_extensions_dict = {}
    for tup in file_extension_tuples:
        for ext in tup[1]:
            file_extensions_dict[ext] = tup[0]
    return lambda ext: file_extensions_dict.get(ext, "Unknown")

```

# Higher order function

`Function that takes another function as an argument`

```py
def square(x):
    return x * x

def my_map(func, args):
    result = []
    for arg in args:
        result.append(func(arg))
    return result

squares = my_map(square, [1, 2, 3, 4] )
```

# map + list()

map, filter and reduce are higher order functions

```py
def square(x):
    return x * x

nums = [1, 2, 3, 4]
squared_nums = map(square, nums)
print(list(squared_nums))
print(map(square, [1, 2, 3, 4])) # This will not work <map object at 0x1004369a0>
```

Map returns a `map object` that is why we need a `list` constructor to convert it to list

```py
def change_bullet_style(document):
    lines = document.split("\n")
    converted = map(convert_line, lines )
    return "\n".join(converted)

# Don't edit below this line

def convert_line(line):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line
```

# filter()

Similar syntax like in map, behaviour same like in js.
We can even use lambda inside like we would use a callback in

```py
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)
# [2, 4, 6]
```

# functools.reduce()

- it needs to be imported before use
- takes two arguments

```py
import functools
def add(sum_so_far, x):
    print(f"{sum_so_far}, x: {x}")
    return sum_so_far + x

numbers = [1, 2, 3, 4]
total = functools.reduce(add, numbers)

print(total)
```

lambda version
💡 In python labda version can only contain single expression!
It means that I can't for example print something and than return like I could in a js callback

```py
number = [1, 2, 3, 4 ]
total = functools.reduce(lambda a, b: a + b, number)

```

# zip

Take to iterables and combine them into a new iterable where each element is a tuple containig one element from each of the original iterables

```py
    a = [1, 2, 3]
    b = [1, 2, 3]


    c = list(zip(a,b))
    # [(1, 1), (2, 2), (3, 3)]
```

💡 Iterables has to be of the same len, if this is not the case, returned element will only return elements where a pair can actually be created:

```py
    a = [1, 2, 3, 4, 5]
    b = [1, 2, 3]

    zipped = zip(a,b)
    # print(type(zipped)) # <class 'zip'>

    c = list(zip(a,b))
    # [(1, 1), (2, 2), (3, 3)]
```

# type(variable)

Returns a type of a variable

# sort() vs sorted()

arr.sort() - mutates original arr
arr.sorted() - returns sorted arr

# Pure functions

In majority of situations you want to use pure functions.

- `Always return the same values given the same arguments`
- `Cause no side effects`

Thanks to this they are predictible, easy to debug, always work the same.
No `works on my machine problem`

Example of pure function

```python
def add(x, y):
    return x + y
    # same result every time
```

Example of impure function:

```python

total = 0
def dirty_add(x):
    global total # this is necessary to access global variable in python
    total = total + x
    return total

print(dirty_add(10)) # 10
print(dirty_add(10)) # 20
print(dirty_add(10)) # 30
    # different result every time, updating global value
```

So why we need to use unpure functions sometimes?
Because we need side effects every now and then.

# Side Effects include:

`Anything that the function does, except returning a value`

- printing to the console
- updating db
- accessing internet
- modyfing global variables or anything outside it's scope (no state mutation)
- modyfing it's input
- writing to a file
- I/O operations

A program that has no side effects is effectively useless.

# References vs Copies

Works almost like in js
Collections are passed as references, `except tuples!`.

When you pass a value into a function as an argument, one of two things can happen:

It's passed by reference: The function has access to the original value and can change it.  
It's passed by value: The function only has access to a copy. Changes to the copy within the function don't affect the original.

These types are passed by reference:

Lists  
Dictionaries  
Sets  
These types are passed by value:

Integers  
Floats  
Strings  
Booleans  
Tuples

Reference:

```py
def modify_list(inner_lst):
    inner_lst.append(4)
    # the original "outer_lst" is updated
    # because inner_lst is a reference to the original

outer_lst = [1, 2, 3]
modify_list(outer_lst)
# outer_lst = [1, 2, 3, 4]
```

No reference

```py

def attempt_to_modify(inner_num):
    inner_num += 1
    # the original "outer_num" is not updated
    # because inner_num is a copy of the original

outer_num = 1
attempt_to_modify(outer_num)
# outer_num = 1
```

# obj.copy()

A way to avoid mutating original object.

```py
def add_format(default_formats, new_format):
    updated = default_formats.copy()
    updated[new_format] = True
    return updated
```

# I/O

The term "i/o" stands for input/output. In the context of writing programs, i/o refers to anything in our code that interacts with the "outside world". "Outside world" just means anything that's not stored in our application's memory (like variables).

All i/o is a form of "side effect". (including print)

In functional programming, i/o is viewed as dirty but necessary.

# No-Op

`Operation that does nothing`

If a function doesn't return anything it is probably impure, and is performing some side effects.

No-Op example:

```py
def square(x):
    x * x
```

Side effect example:

```py
myGlobal = 0

def impure(x):
    global myGlobal
    myGlobal + x
```

The global keyword just tells Python to allow modification of the outer-scoped y variable.

# Memoization

In simple terms memoization is basically storing a copy (caching) of a result of a computation so that we don't have to calculate it again int the future.

```py

def word_count_memo(document, memos):
    memosCopy = memos.copy()

    # Avoid counting again
    if document in memosCopy:
        return memosCopy[document], memosCopy

    count = word_count(document)
    memosCopy[document] = count
    return count, memosCopy

def word_count(document):
    count = len(document.split())
    return count
```

`Pure functions always can be safely memoized and impure can't`
That is why we have dependency array to recalculate memoized val when using useMemo() in React.

`Memoization is not free` - there is always a trade off between using RAM memory and speed. If function is fast enough it should'nt

# Referential Transparency

Pure functions are always referentialy transparent meaning that pure functions can always be replaced by it's would be return value. Since this value is always the same every time.

For example:

```py
add(2, 3)
```

Can simply be replaced with 5

# str to arr

```py
str = 'str'
print(list(str))
```

# sorted with a function

This will be performed on each item
the transformation is only temporary for sorting. The key parameter in sorted() creates a "sort key" - it transforms each element just enough to make comparisons work, but returns the original elements in the sorted order.

```py
def transform_date(date_str):
    month, day, year = date_str.split("-")  # "07-21-2023" -> ["07", "21", "2023"]
    return year + month + day               # -> "20230721"

def sort_dates(dates):
    # sorted() calls transform_date on each date to get sort keys:
    # '07-21-2023' -> '20230721'
    # '12-25-2022' -> '20221225'
    # '01-01-2023' -> '20230101'
    # etc.

    # It sorts by these keys, then returns the ORIGINAL date strings
    return sorted(dates, key=transform_date)
```

# recursion
