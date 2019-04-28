# Explanations

Write a script that allows you to extract your personal schedule from the full exam schedule.

```bash
$ python ./solution.py ../exam-schedule.csv R0661011
24-08-18 Algoritmisch denken
30-08-18 Webontwikkeling 2
29-08-18 Technieken van datamodellering
22-08-18 Computersystemen
```

The order in which the exams are outputted should be the same as in which they appear in the
original file.

The format of the output should be customizable.

```bash
$ python ./solution.py ../exam-schedule.csv R0661011 --format=%c
Algoritmisch denken
Webontwikkeling 2
Technieken van datamodellering
Computersystemen

$ python ./solution.py ../exam-schedule.csv R0661011 --format="`%d at %t %c (location %l)`"
24-08-18 at %t Algoritmisch denken (location D1.16)
30-08-18 at %t Webontwikkeling 2 (location D1.22)
29-08-18 at %t Technieken van datamodellering (location C0.01/C0.02)
22-08-18 at %t Computersystemen (location D0.80 - 1.80)
```

The following placeholders should be supported

<center>

| Placeholder | Meaning |
|-|-|
| `%d` | date |
| `%p` | part of day |
| `%c` | course |
| `%l` | location |
| `%h` | hour |

</center>

In other words, when given a format string such as `%d at %t %c (location %l)`,
`%d` is replaced by the exam's date, `%c` by the exams course, etc.