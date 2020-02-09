# Assignment

Write a function `coins(one, two, five, goal)` that checks
whether it is possible to form the target amount `goal` given
`one`, `two` and `five` coins of denominations 1, 2 and 5, respectively.

E.g. 

* `coins(2, 0, 1, 6)` should return True since 1 coin of denomination 1 and 1 coin of denomination 5 accumulates to the goal 6
* `coins(0, 0, 1, 4)` should return False since 1 coin of denomination 5 cannot accumulate to the goal 4
* `coins(1, 1, 1, 8)` should return True since 1 coin of denomination 1, 1 coin of denomination 2 and 1 coin of denomination 5 exactly accumulates to the goal 8
