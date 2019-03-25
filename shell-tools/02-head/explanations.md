# Explanations

`head` should print the first 5 lines of a given file.

```bash
$ head FILENAME
line 1
line 2
line 3
line 4
line 5
```

If no filename is specified, `head` must gets its data from STDIN.

The option `-n` or `--lines` lets you choose the number of lines to print:

```bash
$ head --lines 10 FILENAME
10 first lines of FILENAME
```