# Assignment

Let's generalize `drop_last`. In a previous exercise, you
had to write `drop_last(xs)` which dropped the last element
of `xs`. But maybe you want to drop the last *two* elements.
Or the *three* last. So, you decide to add an extra parameter:
`drop_last(xs, n)` where `n` indicates how many elements
have to be dropped.

Adding an extra parameter to `drop_last` causes some problems:

* All occurrences of `drop_last(xs)` must be changed to `drop_last(xs, 1)`. This is something you should avoid at all costs: your change breaks other people's code. Also, since this is Python, there's no compiler checking the code and pointing out where parameters are missing, so people will have to manually go through their code.
* While adding more features to a function is not necessarily a bad thing, it does make its usage more complex. In the case of `drop_last`, there's only one extra parameter, but other functions might be extended with multiple parameters. For every such parameter, the user needs to know what value should be passed, even if it's just `0` or `None`.

Is there a way to add this extra parameter without causing so much trouble?

Perhaps you think overloading might be the solution: have two definitions for `drop_last`, one with a single parameter, one with two parameters. However, overloading is not possible in Python (cake point for the first one who can give a reasoned argument why.)

## Default Parameter Values

Python offers a better solution: *default parameter values*. For each parameter of a function, you can specify a default value. If the caller omits this parameter, it will automatically be assigned the associated default value. For example:

```python
def foo(x, y=4):
    return (x, y)

>>> foo(1, 2)
(1, 2)

>>> foo(1)
(1, 4)

>>> foo()
# Error! x is not optional
```

## Keyword Arguments

Say you have the function

```python
def foo(x=1, y=2, z=3):
    return (x, y, z)
```

What if you want to call it with `y` set to 7. You can't use `foo(7)`, because Python will think that you mean to assign `7` to `x`. It seems that the only option is to specify a value for `x` anyway, which means you have to look up what its value should be and then call the function using `foo(1, 7)`.

Luckily, Python supports *keyword arguments* (also called *named arguments*):
when calling a function, you can explicitly tell which parameter is given which value. For example:

```python
foo(y=7)
```

is valid and means "call `foo` with parameter `y` set to `7`." Since all other
parameters have default values, Python won't make a fuss and the result of this call is `(1, 7, 3)`.

This syntax allows you to specify parameter values in any order you want:

```python
def foo(x, y, z):
    return (x, y, z)

>>> foo(z=3, x=1, y=5)
(1, 5, 3)
```
