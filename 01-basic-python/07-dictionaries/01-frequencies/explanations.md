# Assignment

Java calls them `Map`s, JavaScript calls them objects.
Python has chosen to call them *dictionaries*.

Dictionaries are containers that allow you to
store associations between values, commonly called the key and value.
A typical example would be an actual
dictionary, where each word (key)
it is associated with its description (value).
Dictionaries are data structures optimized for
quickly looking up the value associated with a given
key. The other way around is *possible*, but very slow.

A dictionary has the typical operations defined
on them. Skim over the [documentation](https://docs.python.org/3/tutorial/datastructures.html#dictionaries):
it's generally very helpful to have a general
idea of what functions are available to you, so
that when you're working with dictionaries and you
need some specific functionality, you might remember it
already exists.

Write a function `frequencies(xs)` that counts the frequency
of each item in the array `xs` and returns the result as a dictionary.
For example,

```python
>>> xs = [ 'a', 'b', 'b', 'c', 'c', 'c' ]

>>> frequencies(xs)
{ 'a': 1, 'b': 2, 'c': 3 }
```

For this, you'll need to find out the following:

* How to check if a key is present in the dictionary
* How to look up a value
* How to add and update key/value pairs
