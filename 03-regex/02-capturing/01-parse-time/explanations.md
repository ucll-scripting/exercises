# Assignment

Regular expressions have more than one use. Until now, you've only used them
to check if they match a specific pattern.

Say you ask the user for a time of day. You expect it to be in the format
`hh:mm:ss`. To check whether this pattern is satisfied, you write:

```python
if re.fullmatch(r'\d{2}:\d{2}:\d{2}', string):
    ...
```

where `\d` is short for `[0-9]`. Once you've ensured that `string` has
the correct format, you can proceed to extract the hours, minutes and seconds from it.
One way to do this would be:

```python
if re.fullmatch(r'\d{2}:\d{2}:\d{2}', string):
    h, m, s = string.split(':')
```

Simple enough. Now, imagine you also want to introduce milliseconds: `hh:mm:ss.fff` but where the milliseconds are optional. You update your check:

```python
if re.fullmatch(r'\d{2}:\d{2}:\d{2}(\.\d{3})?', string):
    ...
```

Grabbing the components becomes a bit more complex though. You could do it as follows:

```python
if re.fullmatch(r'\d{2}:\d{2}:\d{2}(\.\d{3})?', string):
    if '.' in string:
        left, ms = string.split('.')
        h, m, s = left.split(':')
    else:
        h, m, s = string.split(':')
        ms = '000'
```

It works, but it's certainly not as clean. You can imagine this quickly
becomes more complex with more elaborate patterns.

Luckily, regexes offer functionality to *capture* pieces of the string.
This is done by marking the parts of the pattern you're interested in using
parentheses:

```python
if re.fullmatch(r'(\d{2}):(\d{2}):(\d{2})(\.\d{3})?', string):
    ...
```

This tells the regex engine to store the parts of `string` that match those
patterns. Now, how do we access this data?

`fullmatch` (as well as `match` and `search`) don't return a boolean value.
If the string does not match the pattern, they return `None`, which is a falsey value,
making the `if` condition fail. But if there is a match, a `Match` object is returned, which contains all kinds of interesting information.

Let's take a closer look at our regex:

```text
(\d{2}):(\d{2}):(\d{2})(\.\d{3})?

|-----| |-----| |-----||-------|
   1       2       3       4
```

There are four pairs of parentheses, each of which designate a *group*.
Each group has its own index, starting counting from 1. To get the
strings that corresponds to each group, you can write:

```python
match = re.fullmatch(r'(\d{2}):(\d{2}):(\d{2})(\.\d{3})?', string)

if match:
    h = match.group(1)
    m = match.group(2)
    s = match.group(3)
    ms = match.group(4) or '000'
```

The `or '000'` is necessary because the fourth group is optional: if `string`
were to equal `12:34:56`, then `match.group(4)` would return `None` to indicate
that that part was omitted in `string`. The `or '000'` is equivalent to

```python
ms = match.group(4)

if ms is None:
    ms = '000'
```

This trick is not specific to regexes: you can use it anywhere you
wish to replace a 'missing' value with a default value.

`match.groups()` returns all groups as a tuple, which allows you to shorten your code to

```python
match = re.fullmatch(r'(\d{2}):(\d{2}):(\d{2})(\.\d{3})?', string)

if match:
    h, m, s, ms = match.groups()
    ms = ms or '000'
```

The `groups` method also allows you to specify defaults for missing values:

```python
match = re.fullmatch(r'(\d{2}):(\d{2}):(\d{2})(\.\d{3})?', string)

if match:
    h, m, s, ms = match.groups('000')
```

Now write the function `parse_time(string)` that expects a time with optional milliseconds.
The time can be any stopwatch-based time: e.g. 00:00:00:001, 11:12:13 or 37:42:09.642 all should be valid strings.
If `string` is invalid, the function should return `None`, otherwise it should
return a tuple with four integers representing the hours, minutes, seconds
and milliseconds components of the given time.
