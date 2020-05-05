# Assignment

You are given a file `exam-schedule.csv` which, unsurprisingly, contains an exam schedule.
The goal is to find out how many written exams each lecturer has.

We suggest you take a quick look at its contents.
Each exam has a certain number of properties, among which

* Type of exam (column `Ex. Soortx`). Written exams are identified by an `S` in this column.
* Lecturer id(s) (column `Lector`)

Note that a single row can have one or more lecturers.
If there are multiple lecturers associated with a single exam,
their properties are separated by slashes. For example:

```text
U0075484/U0082713,Billen/Peeters,Clara/Gaby,29-08-18,13:00,nm,MBF13a,ICT en statistiek,2,P,1FVA,R0679987,D1.16
```

This exam has two lecturers associated with it: Clara Billen (U0075484)
and Gaby Peeters (U0082713).

Proceed as follows:

* Consider only rows designating written exams (`S` in column `Ex. Soortx`)
* The exam count for a lecturer equals the number of rows in which that lecturer appears.
* If a row mentions multiple lecturers, add 1 to each lecturer's total count.

For example, consider the following rows (we omitted columns for the
sake of clarity):

```text
U0075484,Billen,Clara,Accountancy 2,S
U0075484,Billen,Clara,Accountancy 2,S
U0075484,Billen,Clara,ICT en statistiek,P
U0075484/U0082713,Billen/Peeters,Clara/Gaby,MBF13a,ICT en statistiek,S
U0075484/U0082713,Billen/Peeters,Clara/Gaby,MBF13a,ICT en statistiek,S
```

These rows describe five exams, but the middle one can be ignored as it's not a written exam.
The first two rows have Clara Billen as lecturer, while the last two rows
have both Gaby Peeters and Clara Billen. The exam counts for these lecturers are:

* Clara Billen (U0075484): 4 written exams
* Gaby Peeter (U0082713): 2 written exams

Once you have processed all rows, you'll have an exam count per lecturer.
Write the results to `output.txt` in increasing order of id.

For example, say the counts are

* U0095814: 103
* U0013579: 177
* U0013031: 15
* U0078121: 44
* U0078896: 45
* U0049910: 87
* U0074065: 99

Ordering them by increasing id and writing them to `output.txt` gives

```text
U0013031 15
U0013579 177
U0049910 87
U0074065 99
U0078121 44
U0078896 45
U0095814 103
```

Note that lecturers without any written exams should not be listed at all.
