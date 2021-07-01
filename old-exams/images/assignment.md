# Assignment

Typically you would know what kind of data a file contains based on its extension.
For example, if a file ends on `.zip`, you know it's a compressed archive.
A `.png` means the file contains an image.
But what happens if the file does not have an extension?

For many file formats, it is possible to look inside the file and determine based on its contents what it actually is.
For example, the 4 first bytes of a png file are always `89 50 4E 47`.
Other file formats can be recognized in different ways.

You are given 100 files named `N.unknown` where `N` varies from 1 to 100.
The only thing you know about these files is that they contain images, but you do not know which format specifically (png, jpeg, gif, etc.)
We want you to write a script that *determines the image format* of each of these files and generates bash commands (see example below) to rename these files so that they have the right extension.
The results should be written to `output.txt`.
The rename commands should be ordered from 1 to 100.

Hint: please do not waste time trying to manually determine the image format yourself. Look for a module.

## Example

Say you find out that `1.unknown` is a jpg, then we want it to be renamed to `1.jpg`.
Now, do *not* actually rename the files.
What you need to do is generate a bash command to rename `1.unknown` to `1.jpg`.
This can be done using the following command:

```bash
mv 1.unknown 1.jpg
```

Produce one such `mv` for each file and write them (in order) to `output.txt`:

```bash
mv 1.unknown 1.jpg
mv 2.unknown 2.gif
mv 3.unknown 3.png
...
```
