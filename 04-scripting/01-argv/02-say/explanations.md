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

In a way, scripts can be seen as functions: they can receive parameters and
perform tasks. Technically, they have return values,
but this is limited to a single integer, the exit code.
In practice, if you need to return something from a script,
this is done by printing out strings or writing data to file.

Adapt the code above so that it prints out the arguments.
The expected behavior is

```bash
$ python say.py hello world
hello world
```

## Shebang

Currently, in order to execute a script, you need to write `python script.py`.
You can shorten this to `./script.py` if you add the following line at the top of your script:

```python
#!/usr/bin/env python
```

Note that this does not work inside all shells. Bash (Git Bash, Linux, MacOS) supports it,
but PowerShell does not. Under MacOS and Linux, you will probably also need
to give execute permissions to your script:

```bash
$ chmod u+x script.py
```

This is completely optional: you'll always be able to run your scripts the
explicit way, i.e., using `python script.py`.