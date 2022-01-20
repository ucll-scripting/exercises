# Assignment

We told you we would be revisiting `contains_duplicates`! This time, you'll implement it using sets.

So, what's a set? Well, let's compare them to lists, as its easier to define sets in terms of their differences.

Lists are boring. They store values, and they keep track of where you put each value.
Lists excel when you ask them 'give me item #5', but that's mostly it. Other operations are rather slow:

* Inserting an element requires all later elements to be moved one spot. Same for deleting elements.
* Checking if an element is in a list is slow: you need to go through the entire list.
  Imagine having to look up a word in a dictionary whose words are not sorted alphabetically.

A set can do all of this much faster. Sets are the best!

Admittedly, there's a catch. You have to give something in return:
sets get to choose themselves how they order their elements internally,
meaning you can't assign indices to elements.
Also, a set can contain an element at most once. Adding some value `x`
to a set that already contains `x` does literally nothing:

```python
>>> xs = { 1, 2, 3 }
>>> xs.add(1)
>>> xs
{1, 2, 3}

>>> xs.add(0)
>>> xs
{0, 1, 2, 3}
```

Now, find a way to implement `contains_duplicates` using a set.
After you have solved this exercise, you can run `benchmark.py`:
it measures the difference in time between a naive implementation and one that uses sets.
You will see the set-based solution easily runs 1000x faster for larger lists.

Below is a JavaScript implementation that uses lists.
More recent version of JavaScript have sets built-in, but you are probably not familiar with them.
Note: see if you can find a way to implement this function using only a single line of code.

```javascript
function containsDuplicates(xs)
{
    const previouslySeen = []; // should be a set

    for ( const x of xs )
    {
        if ( previouslySeen.contains(x) )
        {
            return true;
        }

        previouslySeen.push(x);
    }

    return false;
}
```
