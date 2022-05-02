# Assignment

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

You can solve this with one line of code: first make pairs (tuples of two)
and look for how to [create a dictionary from a list of pairs](https://lmgtfy.app/?q=python+create+dictionary+from+pairs).

```javascript
function fromLists(keys, values)
{
    const result = {};

    for ( let i = 0; i !== keys.length; ++i )
    {
        const key = keys[i];
        const value = values[i];

        result[key] = value;
    }

    return result;
}
```
