# Assignment

I know what you're thinking. You're probably not very impressed by all this regular expression stuff.
Why not simply use `string == 'whatever'`? Much simpler.

Ok, we'll kick it up a notch. Say you want to check if a string consists solely of `a`s?
For example, `"a"` would be fine. Also `"aa"`. Even `"aaaaaa"`. But not `"b"`.

Ordinarily, you would need some sort of a looping construct, something like this:

```python
def one_or_more_a(string):
    return all( char == 'a' for char in string )
```

But now let's do it with regular expressions. How do we express that something can be repeated in regex talk?
Quite simply using the `+` operator of course! The regex `a+` means 'one or more `a`s'.
Note that, contrary to what you're accustomed to, `+` is *not* an infix operator, i.e., you don't put it *between* two things, like `a+b`. The regex `+` is a *postfix operator*, meaning it applies to the element that comes before it, in our case `a`. Note that `a+b` is indeed a valid regular expression: it means "one or more `a`s, followed by one `b`."

Write a function `one_or_more_a(string)` that checks whether `string` consists
of one or more `a`s.
