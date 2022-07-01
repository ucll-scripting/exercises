# Assignment

You receive a json file (`data.json`) containing the birthdays of many people.
We wish to visualize how many birthdays fall in each month and write the result to `output.txt`.

Say, for example, that `data.json` contains

* 1 person whose birthday is in January
* 2 people whose birthday is in February
* 3 people whose birthday is in March

We would visualize this information as follows:

```text
   January *
  February **
     March ***
     April
       May
      June
      July
    August
 September
   October
  November
  December
```

Each asterisk (`*`) represents a single person whose birthday is in the corresponding month.

So, your task is to first count the number of birthdays in each month (Jan-Dec) and then generate a graph exactly like the one shown above but with the correct number of asterisks in each row.

Be sure to respect the layout.
For example, the first column should be exactly 10 characters wide and contain a right-aligned month:

```text
     March ***

|--------|
    10
```

The month name should be followed by exactly one space, after which the right number of asterisks must appear.
