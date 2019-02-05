# Assignment

Write a function `only_digits(string)` that checks whether `string` contains only decimal digits, i.e. `0`, `1`, ..., `9`.
While using the `|`-operator is certainly possible, it is quite clumsy when there are so many allowed options.

Regexes provide *character classes* as a more readable means to describe many single character alternatives:
instead of `a|b|c|d`, you can also write `[abcd]`.

Note that `[abcd]` matches exactly one letter which must be either `a`, `b`, `c` or `d`.
`abcd` is not a match as there are four characters.
