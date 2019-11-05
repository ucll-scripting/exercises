# Assignment

Write a function `median(ns)` that returns the median of the list. To find the median, proceed as follows:

* Sort the array (look up [online](https://docs.python.org/3/library/stdtypes.html) for a built-in algorithm.) Our tests will check that the original order of the list is not changed.
* If `ns` contains an odd number of elements, the median is the middle element. For example, the median of the sorted array `[a, b, c, d, e]` is `c`.
* If `ns` has an even number of elements, the median is the average of the two elements around the centr. For example, the median of `[a, b, c, d, e, f]` is the average of `c` and `d`.

To implement this algorithm, you'll need to determine how long `ns` is.
You will need to look up how, as Python's syntax deviates from other most languages.
