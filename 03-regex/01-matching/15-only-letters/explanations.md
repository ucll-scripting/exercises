# Assignment

Write a function `only_letters(string)` that checks whether `string` contains only letters. Both lowercase and uppercase
are allowed.

We now need to list 52 possibilities. Even with our recently discovered character classes,
this would be a bit too much.

Fortunately, character classes also allow you to specify ranges. For example,
`[a-e]` is equivalent with `[abcde]`. A more complex example is
`[aeiou0-9]`: this matches a single lowercase vowel or digit.