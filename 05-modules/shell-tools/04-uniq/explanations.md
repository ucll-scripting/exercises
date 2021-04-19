# Explanations

`uniq` reads lines and removes all duplicated lines that follow each other.
For example, if given as input

```
a
a
a
b
b
a
a
a
```

`uniq` outputs

```
a
b
a
```

## Options

* `uniq` optionally takes a filename as command line argument.
  If no such argument is provided, it will read its input from STDIN.
* The flag `--ignore-case` (or `-i` for short) should compare lines without taking case into account.

## Examples

```bash
# Removes all consecutive duplicates from foo.txt
$ py uniq.py foo.txt

# Removes all consecutive duplicates from foo.txt (using piping)
$ cat foo.txt | py uniq.py

# Ignores case when comparing lines
$ py uniq -i foo.txt
```
