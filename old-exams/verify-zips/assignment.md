# Assignment

The directory `data` contains a number of zip files.
Each of these zip archives is supposed to contain three files:

* `file-a`
* `file-b`
* `file-c`

However, some will be missing one or more of these files, or contain other unwanted files.
Your job is to identify these faulty zips and list them.
Write a script that produces a file `output.txt` that lists all these faulty zip files in alphabetical order.

## Example

Say we have these zip files with contents

* `sub000.zip`
  * `file-a`
  * `file-b`
  * `file-c`
* `sub001.zip`
  * `file-a`
  * `file-b`
  * `file-c`
  * `extra`
* `sub002.zip`
  * `file-a`
  * `file-c`

The archive `sub000.zip` is correct: is contains the three expected files and only those files.
`sub001.zip` is incorrect: the file `extra` should not be there.
`sub002.zip` is also incorrect: it misses `file-b`.

In this situation, `output.txt` should contain

```text
sub001.zip
sub002.zip
```
