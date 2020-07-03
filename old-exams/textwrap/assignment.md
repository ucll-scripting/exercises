# Assignment

You are given a file `input.txt`.
It contains exactly one line of text, albeit a very long one.
This line consists of words separated by spaces.

You have to *wrap* this text, i.e., break it up in multiple lines so that every line is at most 40 characters long.
Each line must contain as many words as possible, so you can't just have one word per line.

## Example

For clarity's sake, let's pretend the maximum length of a line is 10.
Say `input.txt` contains the following text:

```text
1234 123 12345 1 12 12345678 1 123456789
```

Your script should generate the following `output.txt`:

```text
1234 123
12345 1 12
12345678 1
123456789
```

## Hint

Look for a library.
A solution can be written in a single line of code (excluding the importing of the library).
