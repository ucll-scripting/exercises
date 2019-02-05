# Assignment

Write a function `thrice_repeated(string)` that checks if `string`
consists of three repetitions of the same character, e.g., `aaa`, `555` of `...`.

To solve this, you will need *backreferences*. These allow you
to refer to something encountered earlier in the string.
In essence, to solve this exercise, you want to express the following:

* Match a single character. Since there are no restrictions on what this character can be,
  we use `.` to represent this.
* This next character must be followed by *the same character* encountered earlier.
