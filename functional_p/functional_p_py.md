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

```py
return clean_windows(add_gas(create_car()))
```

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
```
