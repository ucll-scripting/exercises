# Assignment

`digitSum` computes the sum of all the decimal digits of a given number `n`.
For example, `digitSum(159)` returns `15` because 1+5+9=15.

```javascript
function digitSum(n)
{
    let result = 0;

    while ( n > 0 )
    {
        result += n % 10;
        n = Math.floor(n / 10);
    }

    return result;
}
```

Translate this function into Python.
