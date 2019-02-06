# Assignment

Let's start with a simple function that returns `0`.

```python
def zero():
    return 0
```

Note that Python is *whitespace sensitive*: indentation replaces
the need for curly braces. For example, the following code is invalid:

```python
def zero():
return 0
```

The second line is not correctly indented, leading Python to believe
that `return 0` is not part of `zero`'s body.

Now open `student.py` and write a function `five` which simply returns `5`.

To test it, you need to switch to a terminal. First,
let's agree on a simple convention. At times, we will ask of you
to input commands on the terminal. We will write this as follows:

```bash
$ command
output of command
```

The `$` indicates that you are required to input the text  on that line. Lines not prefixed
with `$` represent expected output. For example:

```bash
$ echo Hello world
Hello world
```

Now, to test your `five` function, enter the following command in this directory:

```bash
$ scripting test
PASS 1
FAIL 0
SKIP 0
Score: 1.0/1
```
