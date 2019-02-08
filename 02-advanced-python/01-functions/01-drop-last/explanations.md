# Assignment

Let's generalize `drop_last`. In a previous exercise, you
had to write `drop_last(xs)` which dropped the last element
of `xs`. But maybe you want two drop the last *two* elements.
Or the *three* last. So, you decide to add an extra parameter:
`drop_last(xs, n)` where `n` indicates how many elements
have to be dropped.

Adding an extra parameter to `drop_last` causes some problems:

* All occurrences of `drop_last(xs)` must be changed to `drop_last(xs, 1)`. This is something you should avoid at all costs: your change breaks other people's code. Also, since this is Python, there's no compiler checking the code and pointing out where parameters are missing, so people will have to manually go through their code.
* While adding more features to a function is not necessarily a bad thing, it does make its usage more complex. In the case of `drop_last`, there's only one extra parameter, but other functions might be extended with multiple parameters. For every such parameter, the user needs to know what value should be passed, even if it's just `0` or `None`.

Is there a way to add this extra parameter without causing so much trouble?

Perhaps you think overloading might be the solution: have two definitions for `drop_last`, one with a single parameter, one with two parameters. However, overloading is not possible in Python (cake point for the first one who can give a reasoned argument why.)

Python offers a better solution: *default parameter values*. For each parameter of a function, you can specify a default value. If the caller omits this parameter, it will automatically be assigned the associated default value.
