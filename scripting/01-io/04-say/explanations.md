# Assignment

When you're launching a script from the shell, you can pass along arguments.
For example:

```bash
$ python say.py a b c d
```

These parameters (here four of them, `a`, `b`, `c` and `d`) are
made available to the script through the `sys.argv` array.
Try out the following:

```python
# File say.py
import sys

print(sys.argv)
```

```bash
$ python say.py a b c d
```

In a way, scripts can be seen as functions: the can receive parameters and
perform certain tasks. Technically, they have return values,
but this is limited to a single integer, the exit code.
In practice, if you need to return something from a script,
this is done by printing out strings or writing data to file.

Adapt the code above so that it prints out the arguments.
The expected behavior is

```bash
$ python say.py hello world
hello world
```
