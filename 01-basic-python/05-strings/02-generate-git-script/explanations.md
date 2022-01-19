# Assignment

Write a function `generate_git_script(id)` that generates the following string:

```bash
if [ ! -d id ]; then
    git clone https://github.com/id/project id
else
    (cd id; git pull)
fi
```

where all four occurrence of `id` are replaced by the argument.

We don't provide a JavaScript version: this exercise relies on functionality
that is not readily available in JavaScript.

## Multiline strings

The exercise expects you to produce a multiline string. While it is certainly
doable to put everything into a long string using `\n` to separate lines,
this approach is unacceptably prone to errors. Instead,
we insist on having the ability to drop the string as-is
directly into our code with minimal modifications.
Readability and correctness are of paramount importance; you shouldn't be making any
concessions regarding these.

Python supports multiline strings. Instead of using `"..."` as string
delimiters, use `"""..."""`. You can also prefix them with `f` so as to activate string interpolation.

## String-Related Functionality

Typically, a multiline string will appear inside a function.
Python's syntax rules require a function's body to be indented.
It makes sense that the contents of the string are also indented:

```python
def foo():
    string = '''
    a
    b
    c
    '''
    return string
```

`foo()` is now returns

```text

    a
    b
    c

```

while in reality, you might have preferred

```text
a
b
c
```

In other words, there are leading spaces on each line as well
as redundant lines. You could get rid of these by altering
the string literal:

```python
def foo():
    string = '''a
b
c'''
    return string
```

but this is rather confusing to make sense of. We'd rather avoid this approach.
We'd rather have a correct string that is still readable in code.

The [`dedent` function](https://docs.python.org/3.1/library/textwrap.html) from
the `textwrap` module might come in handy: it removes the undesired leading spaces
from each line. To make use of it, add the following line at the top of your source file:

```python
from textwrap import dedent
```

[The `strip` method](https://docs.python.org/3/library/stdtypes.html#str.strip) will get
rid of the redundant surrounding empty lines for you.
