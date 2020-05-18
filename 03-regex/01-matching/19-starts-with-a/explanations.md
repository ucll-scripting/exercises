# Assignment

As discussed before, Python provides the following functions:

* `re.fullmatch(regex, string)` expects the entire `string` to match `regex`.
* `re.search(regex, string)` expects part of `string` to match `regex`.

There is a third function that checks if the *beginning* of `string` matches `regex`.
Look for it in the [Python docs](https://docs.python.org/3/library/re.html) and use it to solve this exercise.

Write a function `starts_with_a(string)` that checks whether `string` starts with an `a`.
