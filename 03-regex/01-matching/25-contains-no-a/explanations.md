# Assignment

Write a function `contains_no_a(string)` that checks that `string` does not contain the letter `a`.

To solve this problem, you could of course enumerate all characters *except* `a`, but that
would result in quite a long regex. Luckily, there is a shorter way: *negated character classes*.
Look up the syntax and use it to implement `contains_no_a`.
