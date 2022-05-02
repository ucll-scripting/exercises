# Write your code here
"""# Assignment

Write a function `from_lists(keys, values)` that constructs
a dictionary from a list of keys and a list of values.
The `i`-th element of `keys` must be associated with the `i`-th
element of `values`. For example,

```python
>>> xs = [ 1, 2, 3 ]
>>> ys = [ 'un', 'deux', 'trois' ]
>>> from_lists(xs, ys)
{ 1: 'un', 2: 'deux', 3: 'trois' }
```

You can solve this with one line of code. Hint: first make pairs (tuples of two)
and look for how to create a dictionary from a list of tuples."""
def from_lists(keys,values):
    tup = list(zip(keys,values))
    return dict(tup)




