# Assignment

We want to go see a movie together.
Unfortunately, it is probably impossible to find a day on which we all are available.
We will have to settle with trying to find a day on which as many people as possible are free.

A _doedel_ (we don't want to get sued for trademark infringement) is a tool to help with determining this day.
Each person is shown the days the movie plays in theaters and indicates which days they would be able to join.

The file `input.csv` contains the results.
As the extension gives away, it is a CSV file.
The first column contains the person's name.
Each subsequent column represents a date (the first line in the file shows which dates).
If a person is available on a given day, the corresponding column contains a `yes`, otherwise a `no`.

Write a script that lists all dates and the number of `yes` votes on that date:

```text
date1 yescount1
date2 yescount2
date3 yescount3
...
```

The list should be ordered in decreasing order by number of `yes` votes.
You can assume no two days have the same number of `yes` votes.
The output of this script should be written to a file named `output.txt`.

## Example

Say the input file contains

```csv
name,01-06-2021,02-06-2021,03-06-2021
Molly Taylor,no,no,no
Joshua Wade,yes,no,yes
Traci Morris,no,yes,yes
Jennifer Harris,yes,no,yes
```

According to this data, the movie is only in theaters for three days: the first, second and third of June.
If we count the number of yes-votes by date, we get

```text
01-06-2021 2
02-06-2021 1
03-06-2021 3
```

We order by number of yes-votes:

```text
03-06-2021 3
01-06-2021 2
02-06-2021 1
```

The above three lines should be written to `output.txt`.
