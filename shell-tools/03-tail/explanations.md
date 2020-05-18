# Explanations

`tail` should print the last 5 lines of a given file.

```bash
$ tail FILENAME
5 last lines of FILENAME
```

If no filename is specified, `tail` must gets its data from STDIN.

The option `-n` or `--lines` lets you choose the number of lines to print:

```bash
$ head --lines 10 FILENAME
10 last lines of FILENAME
```
