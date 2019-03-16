# Assignment

Write a script `remove-comments.py` that removes comments from a given list of source files:

```bash
$ python remove-comments.py file1.py file2.py file3.py ...
```

A `#` denotes comments: everything that follows on the same line is considered comment.
The `#` itself should also be removed.

To test your implementation, create a couple of files with some random contents
and let your script loose on them.

## Opening and Closing Files

Imagine two applications were to write to the same file at the same time.
If they are not aware that another application is interacting
with the same file, chaos could ensue. It's similar to two cooks
using the same pan without realizing it's being used for two dishes at once.
For this reason, files must be "claimed" (or *locked*) by an application. A file claimed
by one application cannot be used by another application.

When an application wants access to a certain file,
it must ask the OS for permission. If the OS determines the file is available for use,
i.e., not claimed by another application, the application receives exclusive access
to the file. This 'requesting access' is referred to as *opening a file*, hence
the name `open` in Python.

After the application is done with the file, it should give up its
claim as soon as possible, thereby allowing other applications
access to the file. This is known as *closing the file*.

The actual rules are a bit more complicated than described above.
For example, a file can be read by multiple applications simultaneously without
problems, so there's no need for exclusive access in this case.
For this reason, an application can tell the OS it only requires
*read access*, which allows other applications to concurrently read the same file.

We mentioned closing the file, which you probably didn't do in the previous exercises,
and neither do the solutions. What's up with that?

The files are actually being closed for you if you make use of
the `with` statement:

```python
with open(filename) as file:
    ...
```

Without it, you'd have to write

```python
file = open(filename)
...
file.close()
```

This approach is quite risky though: something bad could happen
in between the `open` and `close`, causing an exception to be thrown.
In that case, the `file.closed()` line would not be executed.
The `with` statement takes care of this eventuality: whatever
happens in its body, it guarantees the file will be closed.
