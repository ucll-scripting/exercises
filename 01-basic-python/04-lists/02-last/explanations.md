# Assignment

What would happen if you indexate a list with a negative index?
Java would raise its hands in exasperation and throw an exception at you.
JavaScript would probably do something completely unexpected.
But what would Python do?

Some languages (such as Python and Ruby) choose to
assign meaning to negative indexing. Where
indexing with a positive integer starts counting
forward from the beginning of the list,
a negative index starts at the *end* of the list
and moves backwards. For example, `xs[-1]`
yields the last element of `xs`, `xs[-2]` the second to last, etc.

Write a function `last(xs)` that returns the last element of `xs`.

```javascript
function last(xs)
{
    // Rely on negative indexing in Python
    return xs[xs.length - 1];
}
```
