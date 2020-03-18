# Assignment

## Git Example

Command line tools, i.e., programs that can be launched from the shell such as Python scripts,
often offer many options to customize their behavior.

For example, take git: run the line below in the shell to see how
many commands git understands.

```bash
$ git help -a
```

Each of these has a plethora of additional parameters:
just take a look at [the documentation for `git log`](https://git-scm.com/docs/git-log)
to get an idea.

For example, consider the command

```bash
$ git log --author=abel -i --format=%ad .
```

* `log` tells git we wish to view the logs, i.e., the history of the current repository.
* `--author=abel` asks git to only show changes made by an author whose name contains `abel`.
* `-i` indicates that the author pattern is case insensitive, i.e., the author name can contain `abel`, `Abel`, `ABEL`, etc.
* `--format=%ad` asks to only show the time and date of each change.
* `.` means we wish to see only changes made to files in the current directory and its subdirectories.

Apart from `log`, all the other parameters are optional: `git log` would also work, but produces a different output.

We distinguish three kinds of parameters:

* Positional parameters. In the example above, `log` and `.` are positional. They work the same as in Java or JavaScript: their position determines their meaning. For example, `git log .` is correct, `git . log` is not.
* Flags (or switches), such as `-i`. These turn on some options. In our case, it turns on the case insensitive option.
* Options such as `--author=abel` and `--format=%ad`. These have names (`author` and `format`) and expect arguments (`abel` and `%ad`).

Flags and options can be given in any order: `git log --format=%ad -i --author=abel .` has the same
meaning as our original example.

Many flags have two names: a single lettered one and a full string. For example, `-i` is
shorthand for `--regexp-ignore-case`. The short names are prefixed with a single `-`, while full
names are preceded by `--`. Single lettered flags can also be combined: `-a -b -c` can also be written
`-abc`.

## `argparse`

If you were to have to implement all this logic yourself, it'd probably take you quite a while.
Not only that, you'd have to reimplement it for every script.

Fortunately, there are libraries that implement the lion's share for you.
In Python's case, this library is called `argparse`.
You only need to specify what kind of parameters there are and the library will
take care of parsing `sys.argv` for you and package all data into a nice little object.

For example, the `git log` options mentioned above can be implemented as follows
(we ignore that `log` part for clarity's sake):

```python
import argparse

parser = argparse.ArgumentParser(prog='git')
parser.add_argument('location')
parser.add_argument('--author')
parser.add_argument('-i', '--regexp-ignore-case', action='store_true')
parser.add_argument('--format')

# Parses sys.argv and stores parameters in args
args = parser.parse_args()

print(args)
```

Running it yields

```bash
$ python test.py there
Namespace(author=None, format=None, location='there', regexp_ignore_case=False)

$ python test.py -i --format=lalala --author=ady .
Namespace(author='ady', format='lalala', location='.', regexp_ignore_case=True)
```

## Task

Write a script `range.py` with the following parameters:

* Two positional arguments `start` and `end`.
* A switch `-x` or `--exclusive` that indicates whether `end` should be excluded from the range.
* An option `--step=N` that specifies the step.

A few usage examples:

```bash
$ python range.py 1 5
1
2
3
4
5

$ python range.py 1 5 --step=2
1
3
5

$ python range.py 1 5 -x
1
2
3
4
```

You'll probably need the [documentation](https://docs.python.org/3/library/argparse.html)
and consult StackOverflow.
Take small steps. For example:

* Start with just one positional argument and print its value.
* Find a way to tell `argparse` this argument is meant to be an `int`. By default, all arguments are kept as strings.
* Add the second positional argument and print it.
* Print the range.
* Add support for `-x`. Hint: to implement flags, you might need the `action` parameter of `add_argument`.
* Add `--step`.

Take your time to look up information online. The goal of this exercise is not only
to be able to make use of `argparse`, but also to learn how to explore
a new library by experimenting and looking up things online.
