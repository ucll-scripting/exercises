# Assignment

Write a function `is_number(string)` that determines if `string`
represents a valid number. A number consists of a number of digits,
*optionally* followed by a dot and another series of digits.

The dot might prove problematic: `.` already means something in regex-speak.
If you need an actual dot to appear in the string,
you will need to *escape* it: use `\.` instead of `.`

You already know about the following shortcut operators:

* `x*` means the same as `x{0,}`.
* `x+` means the same as `x{1,}`.

There exists another such prefix operator corresponding to `x{0,1}`, i.e.,
expressing that `x` is optional. Look for it in the [documentation](https://docs.python.org/3/library/re.html) and make use of it for this exercise.
