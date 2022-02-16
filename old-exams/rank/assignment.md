# Assignment

Take a peek at `input.json`.
It contains a list of people's scores.
We ask of you to create a ranking: order the people by decreasing score.
In other words, the person with the highest score is ranked #1, the person with the second highest score is ranked #2, etc.

Write your results to a file named `output.txt`.
Each line in this file must be formatted as

```text
RANK NAME
```

The lines must be ordered by increasing rank.

Note: you can assume that each person in the list has a different score.
You don't need to worry about how to order people with equal scores.

## Example

Say `input.json` has the following contents:

```text
[
    {
        "name": "Laura Michael",
        "score": 1482
    },
    {
        "name": "Joshua Park",
        "score": 9106
    },
    {
        "name": "Kristina Jackson",
        "score": 9663
    }
]
```

The corresponding `output.txt` must then contain:

```text
1 Kristina Jackson
2 Joshua Park
3 Laura Michael
```
