# Write your code here
"""# Assignment

Translate this function that drops both the first and last element of `xs`.

```javascript
function dropEnds(xs)
{
    return xs.slice(1, xs.length - 1);
}
```
"""
def drop_ends(xs):
    return xs[1:len(xs) - 1]