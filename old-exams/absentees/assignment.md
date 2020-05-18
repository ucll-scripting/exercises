# Assignment

You are given two lists:

* A list of all students (`all.txt`);
* A list of students who were present at some very important event (`attending.txt`).

Based on these two lists, you are asked to create a list
of all students who were not present at the event, i.e.
students listed in `all.txt`, but not in `attending.txt`.
Write this list to a new file `absentees.txt`.

* Each student is identified by an id.
* The id is case *insensitive*, meaning that `r01` and `R01` refer to the same student.
* It is possible that `all.txt` contains `r01` whereas `attending.txt` contains `R01`. Make sure to handle these differences in case correctly.
* `absentees.txt` should be formatted as follows:
  * One student id per line.
  * All letters should appear in *lowercase*.
  * The ids should appear in the same order as they are listed in `all.txt`.

## Example

Say `all.txt` contains

```text
r01
r02
R03
R04
r05
```

and `attending.txt` contains

```text
r01
R02
r04
```

then you should produce a file `absentees.txt` with the following contents:

```text
r03
r05
```
