# Assignment

Write a function `remove_duplicates(xs)` that returns a new array equal to `xs` but with duplicated
elements removed. The elements in the result must appear in the same order as in `xs`.

Since the order of the elements in the result is of importance, you can't simply put
the elements in a set: this effectively throws away all information regarding order.

It is important you rely on a set to implement this function,
otherwise running the tests will take a very long time.
Using a set, testing should take approximately 1,000,000 steps,
whereas with a list, it would take 5,000,000,000,000 steps.

A few numbers for you to compare:

number of elts | using set | using list
-------------- |-----------|-----------
10,000         | 0.43s     | 1.53s
20,000         | 0.50s     | 4.50s
30,000         | 0.52s     | 9.44s
40,000         | 0.56s     | 16.54s

The tests feed your algorithm a million elements. On this machine, it takes 4s using sets.
Extrapolation predicts it will take 11 hours with a list.