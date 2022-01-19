# Assignment

Extracting a part from a list, also called *slicing*, is a rather common operation.
For this reason, Python has decided to give it its own syntax.
`xs[a:b]` returns a *new* list that contains the elements with indices `a` to (but not including) `b`.

If the slice reaches until the end of the list, you can omit the second index: `xs[a:]`.
Similarly, you can write `xs[:b]` instead of `xs[0:b]`.
`xs[:]` is also valid: it takes a slice of the entire list, meaning it's making a copy of `xs`.

Write a function `drop_first(xs)` that returns a new list equal to `xs`
from whom the first element has been excluded.

```javascript
function dropFirst(xs)
{
    return xs.slice(1);
}
```
