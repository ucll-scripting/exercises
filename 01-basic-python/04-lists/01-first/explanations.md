# Assignment

Often the need arises to keep track of a variable number of values. For this,
you use a container object. Java offers (among other containers) the `ArrayList`,
whereas JavaScript's provides arrays. These are in essence the same data structure,
just with different names.

Python follows suit: it provides the same data structure, but calls them *lists*.
Syntactically, they are very similar to JavaScript's arrays.

Write a function `first(xs)` that returns the first element of a list.
There are no surprises here: your first guess will probably be correct.

```javascript
function first(xs)
{
    return xs[0];
}
```
