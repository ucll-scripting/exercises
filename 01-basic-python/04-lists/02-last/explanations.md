# Assignment

What would happen if you indexate a list with a negative index?
Java would raise its hands in exasperation and throw an exception at you.
JavaScript would probably do something completely unexpected.
But what would Python do?

Some languages (such as Python and Ruby) choose to
assign meaning to negative indexing. Where
indexing with a positive integer starts counting
forward from the beginning of the list,
a negative indexing starts at the *ending* of the list
and moves backwards. For example, `xs[-1]`
yields the last element of `xs`.

Write a function `last(xs)` that returns the last element of `xs`.
