# Assignment

Sometimes, when you're typing some text, you
accidentally type a word twice. Or even thrice.
It happens to the best of us. So let's write a function `remove_repeated_words` that
removes duplicated words.

To accomplish this, you'll need to know a bit more about `sub`:
if your regex contains one or more groups, you can refer
to them in the `sub`'s second parameter. For example:

```python
re.sub(r'(.)', r'\1\1', string)
```

The `.` in the regex matches with any character. The parentheses
around the dot tell `sub` that whatever matches `.` should be remembered.
Next, the `r'\1\1'` in the replacement string expresses that whatever
matched `(.)` needs to be repeated twice. If you were to try
it out in a Python shell, you'd get:

```python
>>> re.sub(r'(.)', r'\1\1', 'abc')
'aabbcc'
```
