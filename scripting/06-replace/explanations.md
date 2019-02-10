# Assignment

Write a script `replace.py` that takes three parameters:

* A regex
* A string
* The name of the file in which all substrings matching the regex should be replaced by the string.

For example,

```bash
$ python replace.py fo+ bar some-file
```

will turn the file

```text
foo fooooo
qux foofo
```

into

```text
bar bar
qux barbar
```