# Assignment

`dictionary.txt` contains a list of all words of some imaginary language.
`text.txt` is a text written in this imaginary language.

Some words appearing in `text.txt`, however, are misspelled and do not occur in `dictionary.txt`.
We want you to find those words and write them out to `output.txt` in alphabetical order.
Important: if the same misspelled word appears multiple times, it should only be written to `output.txt` once!

All words in both `dictionary.txt` and `text.txt` appear in lowercase.
In other case, you don't have to bother with lower vs uppercase.

## Example

Say the contents for `dictionary.txt` is

```text
aaa
bbb
ccc
```text

`text.txt` contains

```text
aaa bbb, xxx. aaa ccc a.
```

The words `xxx` and `a` do not appear in the dictionary.
We write these in alphabetical order to `output.txt`:

```text
a
xxx
```

== Hint

* You can assume a word is a sequence of one or more lowercase letters.
* Make sure to use the right data structure, otherwise it will take a very long time to generate `output.txt`.
  On this machine, it takes less than a second if programmed well.
