# Assignment

Write a function `contains_three_digits(string)` that checks whether `string` contains at least three digits.
`string` is allowed to contain any number of arbitrary characters, as long as three of these characters
are digits. The digits need not be next to each other.

To solve this exercise, you need a way to express 'any character'. The regex symbol
for this is `.`. For example `...` matches strings that consist of exactly three characters.
`.*` literally matches any string.
