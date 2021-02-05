# Explanations

Download [this zip file](http://scripting.leone.ucll.be/data/crack.zip).
It contains a file named `file.txt`, but it is password protected.
Write a script `crack.py` that tries out passwords until it finds one that works.

```bash
# Should print out the contents of file.txt in crack.zip
$ python crack.py
```

Hint: the password consists of 4 lowercase letters.

## Approach

* Find out how to open a file inside a zip archive.
* The password will need to given as raw bytes, not a string. Find out how to convert a string to bytes (using ASCII encoding).
* Find out how to generate all lowercase strings of length 4.
* When given a wrong password, an exception will be thrown. Find out how to catch this exception and ignore it.
