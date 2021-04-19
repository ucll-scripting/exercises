# Assignment

Write a script that converts [`.csv`](https://en.wikipedia.org/wiki/Comma-separated_values) files into [`.json`](https://en.wikipedia.org/wiki/JSON) files.
Use the headers of the `.csv` as keys for the `.json` file as shown in the example below.
## Example

```csv
fname,lname,grade
John,Johnson,15
Anne,Moon,18
```

should be converted into

```json
[
    {"fname": "John", "lname": "Johnson", "grade": "15"},
    {"fname": "Anne", "lname": "Moon", "grade": "18"}
]
```
