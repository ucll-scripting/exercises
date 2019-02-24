# Assignment

Write a function `twice_repeated(string)` that checks if `string`
consists of two repetitions of the same character, e.g., `aa`, `55` of `...`.

## Backreferences

To solve this, you will need *backreferences*. These allow you
to refer to something encountered earlier in the string.
In essence, to solve this exercise, you want to build a regex with the following structure:

* Match a single character. Since there are no restrictions on what this character can be,
  we use `.` to represent this.
* This next character must be followed by *the same character* encountered earlier.

Backreferences allow you to express the second step as follows:

* First, you need to express the first character is important, that it needs to be 'remembered'. You achieve this by putting this pattern between parentheses. In our case, this leads to `(.)`
* In order to refer to whatever matches with `(.)`, you use a backreference `\1`.

This gives you `(.)\1` as regex. However, there's still a small annoying issue you need to deal with.

## Raw Strings

Technically, the regex `(.)\1` is the correct solution to this exercise. Unfortunately, using

```python
def twice_repeated(string):
    return re.fullmatch('(.)\1', string)
```

will not work. Why not?

Say you need a string with a newline in it, for example

```text
a
b
c
```

 In most languages, you can't just add these newlines in a string directly:

 ```java
 // Invalid code
 String str = "a
 b
 c";
 ```

Instead, you need to rely on escape sequences:

```java
String str = "a\nb\nc";
```

Here, the compiler sees the string literal `"a\nb\nc"` and replaces
each occurrence of `\n` by an actual newline. At runtime,
the string is 5 characters long.

`\n` is not the only existing escape sequence. There's also `\t` for tabs,
`\b` for backspace, etc. If you need your string to contain an actual
backslash, you can use `\\`. You can also refer to symbols using their
[ASCII code](http://www.asciitable.com/), e.g. `\42`.

The newline character has decimal code 10. You might expect `\10` to be synonymous with `\n`, but that would of course be too simple: instead, the `\10` is interpreted
as an *octal* value, not decimal. 10 in octal is 12, so `\12` corresponds to the newline character. You can verify this in the Python shell:

```python
>>> '\12'
'\n'
```

So, why do we tell you this? Well, let's go back to our regex: `(.)\1`.
The Python interpreter sees this `\1` and thinks that you mean
to refer to the character with ASCII code 1, so it replaces
`\1` with this character. Next, the regex engine receives
this weird character instead of `\1`, meaning it will not
recognize it as a backreference.

Somehow, you need `\1` to reach the regex engine unscathed. One way would
be to escape the backslash: `\1` thus becomes `\\1`. The Python interpreter
sees `\\1`, recognizes the escape sequence `\\` and replaces it with a single backslash,
resulting in the regex engine receiving `\1`.

Doubling all backslashes solves our problem, but there is a more readable
solution: raw strings. By prefixing a string with `r`, you tell
the Python interpreter to leave the string alone.
For example, whereas `\n` is a string containing a single character (a newline),
`r'\n'` is a string counting two characters: a backslash followed by the letter `n`.

Back to our exercise: you need `(.)\1` to reach the regex engine.
You can achieve this in either of the following ways:

```python
# Using escape sequences
return re.fullmatch('(.)\\1', string)

# Using raw strings
return re.fullmatch(r'(.)\1', string)
```

We strongly advise you to make use of raw strings. It might even
be safer to simply always use raw strings when dealing with
regexes, regardless of whether it is actually necessary.
