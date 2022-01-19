# Assignment

Translate the function below that rotates a given list `xs` by `n` places.
For example, `rotate([1,2,3,4,5], 2)` modifies the list in place so that it becomes equal to `[3,4,5,1,2]`.

```javascript
function rotate(xs, n)
{
    for ( let i = 0; i !== n; ++i )
    {
        const x = xs.shift();
        xs.push(x);
    }
}
```

You will need to look up how to add and remove elements from a list.
