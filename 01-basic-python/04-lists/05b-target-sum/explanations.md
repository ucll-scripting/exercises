# Assignment

Translate the following function that looks for two numbers in `xs` whose sum equals `target`.

```javascript
function targetSum(xs, target)
{
    for ( const x of xs )
    {
        for ( const y of xs )
        {
            if ( x + y === target )
            {
                return true;
            }
        }
    }

    return false;
}
```
