# Assignment

Write a script `remove-comments.py` that removes comments from a given list of source files:

```bash
$ python remove-comments.py file1.py file2.py file3.py ...
```

A `#` denotes comments: everything that follows on the same line is considered comment.
The `#` itself should also be removed.

To test your implementation, create a couple of files with some random contents
and let your script loose on it. Make sure all comments are gone
and that the remainder has been left undisturbed.
