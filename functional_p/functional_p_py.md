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
