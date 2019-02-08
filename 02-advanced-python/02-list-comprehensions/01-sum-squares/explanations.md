# Assignment

Algorithms often do not operate on a single value, but on a list of values.
It is of course always possible to descend into the trenches and start looping over these values one by one, but this quickly becomes unmanageable when algorithms become more complex.

To assist you in dealing with lists, Python provides *list comprehensions*.
Say you have a list of numbers `ns` and wish to construct a new list
containing the squares of the values of `ns`. Using loops this would give

```python
squares = []

for n in ns:
    squares.append(n ** 2)
```

This same algorithm can be written as a list comprehension as follows:

```python
squares = [ n ** 2 for n in ns ]
```

Write a function `sum_squares(ns)` that computes the sum of the squares of `ns`.
Note that Python has a built-in function to compute the sum of a list of numbers.