# Assignment

Another one of Python's built-in data structure is the *tuple*.
In our opinion, it is rather boring: it is mostly exactly the same
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

Also experiment to see what happens if the lists do not have the same size.

## Exercise

```javascript
function isIncreasing(ns)
{
    // Rely on zip
    for ( let i = 0; i + 1 < ns.length; ++i )
    {
        const x = ns[i];
        const y = ns[i + 1];

        if ( x > y )
        {
            return false;
        }
    }

    return true;
}
```
