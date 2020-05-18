# Assignment

Write a function `hide_email_addresses(string)` that replaces
all email addresses occurring in `string` by `***`, as many
asterisks as there are characters in the address.

Solving this one requires delving deeper into `sub`'s capabilities.
Instead of passing a string as second parameter, you can
also pass a function that computes the replacement string.

As an example, let's revisit the previous exercises
and rewrite them using a function replacement parameter.

```python
def remove_trailing_whitespace(string):
    def replace(match):
        return ''

    return re.sub(' +$', replace, string, flags=re.MULTILINE)
```

Here, `''` has been replaced by a function returning `''`.
This is a typical pattern in programming: replace
data with code that produces the same data. Once you
have done that, you can make the function smarter.

Next, `remove_repeated_words`:

```python
def remove_repeated_words(string):
    def replace(match):
        return match.group(1)

    return re.sub(r'([a-zA-Z]+)( \1)+', replace, string)
```

Notice how `replace` accepts an argument: this is a match object
like the one `fullmatch`, `match` and `search` return.
`replace` then asks for the match object for the contents
of the first group, which corresponds to the duplicated word.

Lastly, `correct_dates`:

```python
def correct_dates(string):
    def replace(match):
        m, d, y = match.groups()
        return f'{d}/{m}/{y}'

    return re.sub(r'(\d+)/(\d+)/(\d+)', replace, string)
```

Here, `replace` uses the `groups()` method to retrieve
the month, day, and year and returns a string where
they have been reordered.

Now you should be able to write `hide_email_addresses`.
