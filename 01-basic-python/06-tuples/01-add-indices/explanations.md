# Assignment

Another one of Python's built-in data structure is the *tuple*.
Admittedly, it is rather boring: it is mostly exactly the same
as a list, except that it is immutable: once created, you cannot alter
it in any way. This property will come in handy later, when we
deal with dictionaries.

A tuple looks like this:

```python
(1, 2, 3)
```

So, instead of using `[]` as delimiters, you simply uses `()`. That's really it.

## Zipping

The built-in `zip` function takes a number of lists and
groups their first elements together in a tuple, their second elements, etc.
For example, try the following in a Python shell:

```python
>>> xs = [1, 2, 3]
>>> ys = ['a', 'b', 'c']

>>> list(zip(xs, ys))
[(1, 'a'), (2, 'b'), (3, 'c')]
```

`zip` doesn't return its result as a list however, but as a _generator_.
What generators are is not important at this moment.
Suffice it to say you can turn a generator into a list using `list`, e.g., `list(zip(xs, ys))`.

Also experiment to see what happens if the lists do not have the same size.

## Exercise

Translate the function shown below.
Given a list, e.g., `['a', 'b', 'c']` and pairs each element with its index:
`[ [0, 'a'], [1, 'b'], [2, 'c'] ]`.

```javascript
function addIndices(xs)
{
    const result = [];

    // The Python implementation does not require a loop
    // Use zip instead
    for ( let i = 0; i !== xs.length; ++i )
    {
        // JavaScript doesn't have tuples, so we represent pairs as arrays
        // Use tuples in Python instead
        result.push( [i, xs[i]] );
    }

    return result;
}
```
