# Assignment

The file `input.json` contains the grades of students for multiple tests throughout the semester in JSON-format.
For example:

```json
[{"id": "r0077959", "grades": [6, 8, 14, 5, 5, 8, 9, 6, 8]},
 {"id": "r0056617", "grades": [10, 13, 12, 19, 19, 18]}]
```

We need you to read in all data and compute the *rounded* average per student.
The formula is

```text
round( sum of all grades / number of grades )
```

For example, student `r0077959` has grades `[6, 8, 14, 5, 5, 8, 9, 6, 8]`,
the sum of which is `69`. Dividing this by the number of grades (`9`) results
in `7.666`. Rounding this gives `8`.

Write the results to a file named `output.txt` using the following format:

```text
r0056617 15
r0077959 8
```

**Important:** the data must appear in increasing order of student id.
