# Assignment

Write a function `countdown(n)` that, given an integer `n`, produces
a string with a countdown from `n` to `1`.
For example,

```python
>>> countdown(5)
"5, 4, 3, 2, 1"
```

Proceed as follows:

* First, find a way to generate a list of decreasing integers such as `[5, 4, 3, 2, 1]`.
* Next, you'll want to convert each of these integers to a string.
  Rely on a list comprehension for this.
  You should end up with `['5', '4', '3', '2', '1']`.
* Finally, you should combine these strings into one big string, using `', '` as separator.
  This functionality is built-in so don't implement it yourself.
