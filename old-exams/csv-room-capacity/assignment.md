# Assignment

`exam-schedule.csv` contains an exam schedule in csv form.
We'd like to check that none of the rooms are overbooked
by computing the maximum occupancy of every room during the exam period.

Each row in `exam-schedule.csv` represents an exam taken by a single student.
The following columns are relevant to this task:

* `Datum`: date on which the exam takes place.
* `Dagdeel`: part of the day the exam takes place on. This is either `vm` (morning),
  `nm` (afternoon) or `av` (evening).
* `Lokaal`: location.

Let's combine the day and the part of day field into a single concept
which we'll call an *exam moment*. Examples of exam moments
are "27-8-2018 vm" and "31-8-2017 nm".

Your task will be to count how many students are
allocated to a specific room per exam moment.
Consider for example the following rows (irrelevant columns have been
omitted for the sake of clarity)

```csv
01-09-18,vm,D0.60 (Hemisfeer)
01-09-18,vm,D0.60 (Hemisfeer)
01-09-18,vm,D0.60 (Hemisfeer)
01-09-18,vm,D0.60 (Hemisfeer)
01-09-18,nm,D0.60 (Hemisfeer)
01-09-18,nm,D0.60 (Hemisfeer)
02-09-18,vm,D0.60 (Hemisfeer)
02-09-18,vm,D0.60 (Hemisfeer)
02-09-18,vm,D0.60 (Hemisfeer)
01-09-18,vm,C0.01/C0.02
01-09-18,vm,C0.01/C0.02
01-09-18,vm,C0.01/C0.02
01-09-18,vm,C0.01/C0.02
01-09-18,vm,C0.01/C0.02
```

Let's add blank lines to group blocks of exams together that
take place on the same moment and in the same location.

```csv
01-09-18,vm,D0.60 (Hemisfeer)
01-09-18,vm,D0.60 (Hemisfeer)
01-09-18,vm,D0.60 (Hemisfeer)
01-09-18,vm,D0.60 (Hemisfeer)

01-09-18,nm,D0.60 (Hemisfeer)
01-09-18,nm,D0.60 (Hemisfeer)

02-09-18,vm,D0.60 (Hemisfeer)
02-09-18,vm,D0.60 (Hemisfeer)
02-09-18,vm,D0.60 (Hemisfeer)

01-09-18,vm,C0.01/C0.02
01-09-18,vm,C0.01/C0.02
01-09-18,vm,C0.01/C0.02
01-09-18,vm,C0.01/C0.02
01-09-18,vm,C0.01/C0.02
```

* The first 4 lines take place on exam moment "01-09-18 vm" in D0.60.
* The next 2 take place on exam moment "01-09-18 nm", again in D0.60.
* The next 3 take place on exam moment "02-09-18 vm", again in D0.60.
* The last 5 take place on exam moment "01-09-18 vm" in C0.01/C0.02.

We can determine the maximum occupancies for each location:

* The maximum occupancy for D0.60 is 4, namely on 01-09-18 vm.
* The maximum occupancy for C0.01/C0.02 is 5.

Output this information to `output.txt` in the following form:

```text
C0.01/C0.02 5
D0.60 (Hemisfeer) 4
```

The lines need to appear in alphabetical order.
