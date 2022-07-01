# Assignment

`input.txt` contains text in which many small calculations appear.
These calculations have the form `${a+b}` or `${a*b}`.
Replace all these calculations by their result.
For example, `${1+2}` should be replaced by `3`.

* Only addition and multiplication will be used.
* Numbers can consist of many digits.
* Spaces can appear inside the calculations, e.g. `${ 12 + 78 }` or `${17   + 3    }`.
* All text surrounding the calculations has to be left unmodified.

Write the results to `output.txt`.

## Example

Say `input.txt` has the following contents:

```text
dfjkldf ${1+2} fjdkjf sdfjkdl sf ${ 2 * 3 } fjdlkf
qiopf fmnkan ${ 1111 + 2222} jqlkjlfppmvpamd
```

Three calculations appear in this text.
Replacing them with their results should yield the file `output.txt` with contents

```text
dfjkldf 3 fjdkjf sdfjkdl sf 6 fjdlkf
qiopf fmnkan 3333 jqlkjlfppmvpamd
```
