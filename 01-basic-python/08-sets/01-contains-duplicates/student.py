# Write your code here
"""```javascript
function containsDuplicates(xs)
{
    const previouslySeen = []; // should be a set

    for ( const x of xs )
    {
        if ( previouslySeen.contains(x) )
        {
            return true;
        }

        previouslySeen.push(x);
    }

    return false;
}
```
"""
def contains_duplicates(xs):
    return len(xs) != len(set(xs))
