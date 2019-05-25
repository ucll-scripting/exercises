# Assignment

Write a script `find.py` that prints out all files and directories
that satisfy certain conditions.

The following functionality must be supported:

* One positional parameter that specifies the directory in which to start looking recursively.
* `--minimum-size=N`: only files whose size is at least `N` must be listed.
* `--maximum-size=N`: only files whose size is at most `N` must be listed.
* `--no-directories`: don't list directories.
* `--no-files`: don't list files.
* `--extension=EXT`: only list entries with extension `EXT`
* `--contains=REGEX`: only list files whose contents match `REGEX`.

To get a better feel for how your script should work, feel free
to experiment with the solution. For example, try

```bash
# List everything starting from two directories up
$ python find ../..

# List all python files in current directory
$ python find --extension=.py .
```
