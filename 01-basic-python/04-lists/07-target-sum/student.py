# Write your code here
"""
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
"""
def target_sum(xs, target):
    for x in xs:
        for y in xs:
            if x + y == target:
                return True
    return False                