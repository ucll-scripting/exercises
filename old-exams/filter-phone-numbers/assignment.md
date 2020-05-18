# Assignment

`input.txt` contains a list of phone numbers. Extract all
valid Belgian cell phone numbers and write them to `output.txt`.

The validity is determined by the following rules:

* The phone number is structured as follows: `ABBB-CC-DD-EE`.
* Part A is either `+32` or `0`.
* Part B is a three digit number ranging from `450` to `499`.
* Next come three numbers `C`, `D` and `E` of two digits each.
* Note that if part A is `+32`, there should be an extra dash between parts A and B.
  For example, `+32-476-12-34-56` and `0476-12-34-56` are valid, but
  `+32476-12-34-56` and `0-476-12-34-56` are not.

The phone numbers in `output.txt` should appear in the same order as in `input.txt`.

## Examples

Say `input.txt` contains the following data (the text after `#` is not part of the file)

```text
+32-477-12-34-56        # Valid
0485-11-22-33           # Valid
0-475-11-22-33          # Invalid: there should be no dash between 0 and 475
+32477-12-34-45         # Invalid: there should be a dash between +32 and 477
+32 477 11 23 55        # Invalid: spaces should be dashes
+31-499-54-64-87        # Invalid: +31 is not allowed
0478-78-89-451          # Invalid: too many digits in last part
+32-487-99-99-99        # Valid
```

You should then generate `output.txt`:

```text
+32-477-12-34-56
0485-11-22-33
+32-487-99-99-99
```
