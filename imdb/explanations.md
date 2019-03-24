# Explanations

Run the script `prepare.py`, which downloads [IMDb](https://www.imdb.com/) data in tsv form (tab separated values).
Find a Python module that can help you easily parse this data. Hint: tsv and csv (comma separated values) are quite related.

Run `solution.py`:

```bash
$ python solution.py > expected.txt
```

It might take a while before it's ready. Your task is to write a script that produces the same output.
Use the python library named `tabulate` to produce tables.
You can install it as follows:

```bash
$ pip install tabulate
```

You can check if your own script produces the correct output with the following commands:

```bash
$ python my-script.py | diff - expected.txt
```

`diff` will show the differences between your output and the expected output. If it doesn't print anything,
your script is fully correct.