# Assignment

Translate the following function:

```javascript
function containsDuplicates(xs)
{
    for ( let i = 0; i !== xs.length; ++i )
    {
        for ( let j = i + 1; j < xs.length; ++j )
        {
            if ( xs[i] === xs[j] )
            {
                return true;
            }
        }
    }

    return false;
}
```
