# Write your code here
"""
# Assignment

Translate this function that returns the middle element.

```javascript
function middle(xs)
{
    // Look up how to find a list's length in Python
    const index = Math.floor(xs.length / 2);

    return xs[index];
}
```

"""
def middle(xs):
    middle = len(xs)//2
    return xs[middle]
    