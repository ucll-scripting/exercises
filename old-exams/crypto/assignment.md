# Assignment

You are given a file `input.json` which contains data in JSON format.
Take a quick peek at it.
As you can see, it contains a list of cryptocoin related data represented as a list of objects, each with a `currency` and `history` field.
The history is a long series of numbers representing currency rates throughout time.

We want you to write a script that summarizes this data.
For each cryptocoin in the input file, determine the lowest, highest and current rate (= the last one in the history.)
Write this information to a file named `output.txt`.
For every cryptocoin, there should be one line formatted as shown below:

```text
currency minimum maximum current
```

The currencies in the output file have to appear in the same order as they do in the input file.

## Example

Say `input.json` contains the following data:

```json
[
    {
        "currency": "bitcoin",
        "history": [ 1, 1, 2, 3, 1000, 55000, 50000, 30000 ]
    },
    {
        "currency": "ucll-coin",
        "history": [ 1, 1, 1, 1, 1 ]
    }
]
```

Your script needs to process each coin in turn.

The first currency is `bitcoin`.

* `1` is the lowest rate
* `55000` is the highest rate
* `30000` is current rate.

We output this data as

```text
bitcoin 1 55000 30000
```

Similarly, the second coin can be summarized as

```text
ucll-coin 1 1 1
```

These two lines need to be written to a file named `output.txt`:

```text
bitcoin 1 55000 30000
ucll-coin 1 1 1
```
