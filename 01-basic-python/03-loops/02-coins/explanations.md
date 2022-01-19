# Assignment

Write a function `coins(one, two, five, goal)` that checks
whether it is possible to form the target amount `goal` given
`one`, `two` and `five` coins of denominations 1, 2 and 5, respectively.

```javascript
function coins(one, two, five, goal)
{
    for ( let x = 0; x <= one; ++x )
    {
        for ( let y = 0; y <= two; ++y )
        {
            for ( let z = 0; x <= five; ++z )
            {
                if ( x + 2*y + 5*z === goal )
                {
                    return true;
                }
            }
        }
    }

    return false;
}
```
