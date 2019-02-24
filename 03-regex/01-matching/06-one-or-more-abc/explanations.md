# Assignment

What if we want `abc` to be repeated one or more times?

* `abc+` would not work: the `+` only applies to the `c`. In other words, `abcccc` would match, but that's not what we want.
* `a+b+c+` is not correct either. This would result in `aaaabbbcccc`, not `abcabcabc`.

We need the `+` operator to apply on all three letters `abc`. Like in mathematics, we can achieve this using parentheses: `(abc)+`.

Write a function `one_or_more_abc(string)` that checks whether `string` equals
one or more times `abc`.