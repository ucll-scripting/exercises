# Assignment

The list below is increasing

```text
1 2 3 4 5
```

This one is decreasing:

```text
9 7 5 4 2 1
```

Now take this list:

```test
1 4 6 8 7 5 4 2 1
      ^
```

At the indicated position, the list 'changes its mind' and switches
from increasing to decreasing. We say that it has taken 'a turn.'.
The list below has two turns:

```text
1 2 3 4 5 4 3 2 1 2 3 4 5 6
        ^       ^
```

Write a function `count_turns(ns)` that counts the number of turns in a list of numbers.
Make use of `zip` knowing that it can take an arbitrary number of arguments.

Also, Python is one of the few languages where you can chain comparison operators:
`a < b < c` yields `True` if `a` is less than `b` and `b` is less than `c`.

If consecutive numbers are equal, we do not count that as a turn.
