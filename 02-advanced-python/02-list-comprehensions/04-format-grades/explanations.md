# Assignment

Say you receive a dictionary that associates names with lists of grades.
For example,

```python
{ 'John': [10, 10, 10], 'Ann': [12, 14], 'Nick': [17, 18, 18] }
```

Given this information you need to construct a string containing the end results per student. The end result for a student
equals the *rounded* average of his or her grades. This gives:

```python
John: 10
Ann: 13
Nick: 18
```

Write a function `format_grades(grades)` that, given a dictionary with grades per student,
returns a string as shown above.

Suggested approach:

* Focus first on taking the average.
  Define a function `average` that receives a list of numbers and returns the rounded average.
* We want to process each student in turn.
  Find a way to iterate over a dictionary and get access to all key/value pairs.
* Combine the previous two steps into one functioning solution.
