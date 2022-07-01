# Assignment

`input.txt` contains a JSON-string with hourly temperature recordings for each day in 2019.
Write a script that computes the average temperature (rounded to the closest integer) of each day and prints them out in chronological order.

* Dates are formatted as day/month/year.
* The temperatures appear in random order; you'll have to sort them by date.

## Example

For brevity's sake, let's say `input.txt` only contains temperatures for 4 dates:

```json
{
    "01/12/2019": [-1, 0, 2, 2, 4, 5, 8, 8, 10, 11, 13, 13, 14, 14, 12, 10, 10, 9, 6, 5, 4, 2, 1, 0],
    "01/04/2019": [1, 1, 2, 4, 4, 6, 7, 8, 9, 9, 10, 12, 16, 17, 16, 14, 10, 10, 9, 7, 7, 5, 3, 1],
    "01/01/2019": [-5, -5, -4, -2, -1, 3, 4, 6, 7, 8, 10, 10, 11, 12, 10, 10, 8, 7, 6, 3, 2, 0, -2, -5],
    "01/08/2019": [5, 6, 6, 7, 7, 8, 9, 12, 15, 16, 18, 25, 30, 32, 31, 32, 29, 27, 23, 19, 18, 15, 14, 11]
}
```

First, you'll have to sort them by date, which gives:

```text
"01/01/2019": [-5, -5, -4, -2, -1, 3, 4, 6, 7, 8, 10, 10, 11, 12, 10, 10, 8, 7, 6, 3, 2, 0, -2, -5],
"01/04/2019": [1, 1, 2, 4, 4, 6, 7, 8, 9, 9, 10, 12, 16, 17, 16, 14, 10, 10, 9, 7, 7, 5, 3, 1],
"01/08/2019": [5, 6, 6, 7, 7, 8, 9, 12, 15, 16, 18, 25, 30, 32, 31, 32, 29, 27, 23, 19, 18, 15, 14, 11],
"01/12/2019": [-1, 0, 2, 2, 4, 5, 8, 8, 10, 11, 13, 13, 14, 14, 12, 10, 10, 9, 6, 5, 4, 2, 1, 0],
```

Next, compute the average (also called mean) of the temperatures.

```text
4
8
17
7
```

The above four lines are to be written to `output.txt`.

## Hints

* As always, take it step by step. Implement each step separately using dummy data.
* Start by determining how to **parse** the JSON-string, which will in this case yield a dictionary.
* You need to sort the data. You will need to convert the dictionary into a list of key/value pairs.
* You will then need to sort this list based on the first element of each pair.
* While you can take care of the comparing dates yourself, it is far easier to rely on an existing Python class. You need to find a way to **parse** a string such as `"01/01/2019"` into a date object and let that handle the comparison for you.
* Look for a function that computes the mean value of an array.
