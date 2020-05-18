# Assignment

The file `input.txt` contains a list of names.
We need you to transform this list of names
into a list of e-mail addresses, following these rules:

* For each name in `input.txt`, split it up in a first name and a last name.
  You can assume that the first name only contains letters (i.e. no dashes or spaces).
* The e-mail address is formed as `fname.lname@student.ucll.be`,
  where `fname` is the student's first name in lowercase and `lname`
  is the student's last name in lowercase where all parts are joined together.
  E.g. `Van den Briel` becomes `vandenbriel`.
* The e-mail addresses need to be listed in the same order as their corresponding names.

Write the resulting list of e-mail addresses to `output.txt`.

## Example

If `input.txt` contains

```text
Nikita Massie
Axel Kazantsev
Abel Vanbriel
Jasper Van den Briel
```

then you need to generate an `output.txt` with

```text
nikita.massie@student.ucll.be
axel.kazantsev@student.ucll.be
abel.vanbriel@student.ucll.be
jasper.vandenbriel@student.ucll.be
```
