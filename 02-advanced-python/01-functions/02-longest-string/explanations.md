# Assignment

Write a function `longest_string(strings)` that, given a list of strings, returns the longest one.

This is kind of like finding a maximum, but not quite. Using `max(strings)` would
return the string that comes last alphabetically: `max('z', 'aaa')` yields `z`.
So, we cannot rely on `max`. Or can we?

`max` has one of those fancy optional parameters. It's called `key` and it allows you to fine-tune
how the function decides what is the greatest value. `key` must be bound to a function
which returns the property that should be maximized. An example might make this clearer.

Say we have a list of `Person` objects. Each person has an age, a height and a weight.
We want to find:

* The oldest person
* The tallest person
* The heaviest person

All three can be found by relying on the `key` parameter of `max`:

```python
def by_age(person):
    return person.age

def by_height(person):
    return person.height

def by_weight(person):
    return person.weight

oldest = max(people, key=by_age)
tallest = max(people, key=by_height)
heaviest = max(people, key=by_weight)
```

This can be written more concisely using lambdas:

```python
oldest = max(people, key=lambda p: p.age)
tallest = max(people, key=lambda p: p.height)
heaviest = max(people, key=lambda p: p.weight)
```

Or you can rely on `itemgetter`:

```python
from operator import itemgetter

oldest = max(people, key=itemgetter('age'))
tallest = max(people, key=itemgetter('height'))
heaviest = max(people, key=itemgetter('weight'))
```

Now you should be able to solve the exercise using a single line of code.
