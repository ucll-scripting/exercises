# Assignment

`input.txt` contains a list of dates. However, many of them
are invalid. We ask of you to copy all valid dates to a separate
file named `output.txt`.

A valid date satisfies the following constraints:

* It consists of three numbers separated by dashes (`-`).
* The three numbers represent day, month and year, in that order.
* The date itself must exist according to our calendar. You should rely on Python's library for this part.
* When validating the date, make sure there is no trailing new line character in the string.

The dates in `output.txt` must appear in the same order as they do in `input.txt`.

## Example

Consider the following file `input.txt`:

```text
1-1-2000
2/5/1998
12-18-1980
29-2-2009
7-5-2000
```

* The first date is valid.
* The second date is invalid: it uses the wrong separator (`/` instead of `-`).
* The third date is invalid: there is no 18th month.
* The fourth date is invalid: 2009 is not a leap year.
* The fifth date is valid.

`output.txt` should therefore contain

```text
1-1-2000
7-5-2000
```
