# Assignment

Write a function `nth_longest_string(n, strings)` that returns the `n`th longest string.

You could of course repeatedly find the longest string and remove that.
A more straightforward way would be to first sort the list according to string length
and then pick the right element.

Make use of the `sorted` function. Like `max`, it features an optional `key` parameter.