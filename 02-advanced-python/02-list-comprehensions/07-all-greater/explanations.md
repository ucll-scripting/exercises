# Assignment

List comprehensions allow multiple `for` clauses. For example:

```python
>>> [ (x, y) for x in ['a', 'b'] for y in ['1, '2'] ]
[('a', '1'), ('a', '2'), ('b', '1'), ('b', '2')]
```

Write a function `all_greater(ns, ms)` that checks if all elements in `ns` are greater than all elements in `ms`.
