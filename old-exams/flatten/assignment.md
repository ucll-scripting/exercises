# Explanations

Take a look at the contents of `input.txt`. You'll find that it contains lines
of comma separated student ids (no spaces). The goal is to transform this into
a file `output.txt` that contains one id per line.
The order of the ids must be preserved.

## Example

Say `input.txt` contains the following data:

```text
r03,r01
s02,r04,s01
```

Your script must then generate a file `output.txt` with contents

```text
r03
r01
s02
r04
s01
```
