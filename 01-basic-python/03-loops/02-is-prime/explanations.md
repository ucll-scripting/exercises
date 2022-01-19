# Assignment

Write a function `is_prime(n)` that determines if `n` is prime.

```javascript
function isPrime(n)
{
    for ( let k = 2; k !== n; ++k )
    {
        if ( n % k === 0 )
        {
            return false;
        }
    }

    return n > 1;
}
```

* Make use of Python's [`for`-loop](https://lmgtfy.app/?q=python+for+loop).
* In case you need to refer to the boolean value false in your code, know that its [syntax is not `false`](https://lmgtfy.app/?q=python+false).
