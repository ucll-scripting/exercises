"""## Exercise

Translate the function shown below.
Given a list, e.g., `['a', 'b', 'c']` and pairs each element with its index:
`[ [1, 'a'], [2, 'b'], [3, 'c'] ]`.

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
"""
def add_indices(xs):
    return list(zip(range(len(xs)),xs))