# Assignment

Write a function `remove_duplicates(xs)` that returns a new array equal to `xs` but with duplicated
elements removed. The elements in the result must appear in the same order as in `xs`.

Since the order of the elements in the result is of importance, you can't simply put
the elements in a set: this effectively throws away all information regarding order.

It is important you rely on a set to implement this function,
otherwise running the tests will take a very long time.
Using a set, testing should take approximately 1,000,000 steps,
whereas with a list, it would take 5,000,000,000,000 steps.
