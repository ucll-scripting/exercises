# Assignment

The file `input.txt` contains a list of ids.
We distinguish two kinds of ids:

* Student ids: these start with an `s` or an `r`.
* Personnel ids: these start with a `u`.

Note that these prefixes can appear both in lowercase and uppercase.

We ask of you to generate a list of e-mail addresses based
on these ids. The rules are as follows:

* All e-mail addresses must be in lowercase.
* E-mail addresses for students have the form `id@student.ucll.be`.
* E-mail addresses for personnel have the form `id@ucll.be`.

Write the resulting e-mail addresses to a file `output.txt`:

* One address per line.
* The addresses should appear in the same order as their corresponding id occurs in `input.txt`.

## Example

Given an `input.txt`

```text
s0045911
R0067933
R0043469
u0009827
S0056787
```

This should produce a file `output.txt` with the following contents:

```text
s0045911@student.ucll.be
r0067933@student.ucll.be
r0043469@student.ucll.be
u0009827@ucll.be
s0056787@student.ucll.be
```
