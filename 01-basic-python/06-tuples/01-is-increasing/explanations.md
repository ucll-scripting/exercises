# Assignment

Another one of Python's built-in data structure is the *tuple*.
In our opinion, it is rather boring: it is mostly exactly the same
as a list, except that it is immutable: once created, you cannot alter
it in any way. This property will come in handy later, when we
deal with dictionaries.

A tuple looks like this:

```python
(1, 2, 3)
```

So, instead of using `[]` as delimiters, you simply uses `()`. That's really mostly it.

# Zipping

The built-in `zip` function takes a number of lists and
groups their first elements together in a tuple, their second elements, etc.
For example, try the following in a Python shell:

```python
>>> xs = [1, 2, 3]
>>> ys = ['a', 'b', 'c']

>>> zip(xs, ys)
[(1, 'a'), (2, 'b'), (3, 'c')]
```

Also experiment to see what happens if the lists do not have the same size.

## Reasoning Behind Tuples

The reason that tuples exist is more apparent in statically typed languages such as Java or C#. We'll continue our explanation using C# since tuples have a cleaner implementation
than in Java.

In C#, a list is generally represented using an `List<T>`.
This class embodies the same functionality as Java's `ArrayList<T>`.
A `List<T>` contains nothing but `T`s, which is why it is called *homogenous*.
Also, the size of the list can vary during execution; in general, you don't know
ahead of time (while writing code) how many items the `List<T>` will contain.

A tuple differs in two aspects: it is typically *heterogenous* in that
it contains items of different types. This is why, contrary to `List`, the `Tuple` class
has multiple type parameters, e.g., `Tuple<int, string>` or
`Tuple<bool, string, double, Person>`. From this follows that you must know
exactly how many items a tuple contains, since you need to explicitly mention
their types.

Since Python does not have type annotations, this distinction mostly fades away.
Lists and tuples differ mostly in how they are used. For example,
iteration over lists is common, but less so with tuples. This is due
to the fact that lists contain similar items who can be processed
with the same instructions, while tuples tend to contain diverse pieces
of data which do not lend themselves to a single uniform treatment.

## But Could You Please Finally Tell Me What The Assignment Is?

Okay, okay, here it is. As if you couldn't infer it from the name. Some people...

Write a function `is_increasing(ns)` that checks if `ns` is an increasing list of numbers.