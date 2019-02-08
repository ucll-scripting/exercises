# Assignment

Write a function `divisors(n)` that returns a list of all the divisors of `n`.

This exercise requires some kind of filtering: we start off with a list
of numbers from `1` to `n` and then only keep those that
nicely divide `n`.

List comprehensions let you add an `if` clause: only elements
satisfying the condition will be included in the resulting list.
For example:

```python
>>> [ x for x in range(1, 100) if is_prime(x) ]
[ 2, 3, 5, 7, 11, ... ]
```
