# Assignment

Translate the function below that drops the element with index `n`.

```javascript
function dropNth(xs, n)
{
    return [...xs.slice(0, n), ...xs.slice(n+1) ];
}
```

Python allows you to use the `+` operator to concatenate lists:

```python
[1, 2] + [3, 4] == [1, 2, 3, 4]
```

Alternatively, you can also use the `*`-operator that acts like JavaScript's spread operator `...`:

```python
xs = [1, 2]
ys = [3, 4]
zs = [ *xs,  *ys ]
zs == [1, 2, 3, 4]
```
