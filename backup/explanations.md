# Explanations

Write a script for making backups.

```bash
$ python backup.py /c/backups /c/important-files (linux)
$ python backup.py c:/backups c:/important-files (win)
```

should create a file named `YEAR-MONTH-DAY.zip` in the `backups` directory
where the zip contains all files inside the `important-files` root directory.
Inside the archive, the filenames should be relative to this root directory. For example,
say you have the following files:

```text
c
  important-files
    foo
      a.txt
      b.txt
    bar
      baz
        c.txt
```

then the zip should contain

```text
foo/a.txt
foo/b.txt
bar/baz/c.txt
```
