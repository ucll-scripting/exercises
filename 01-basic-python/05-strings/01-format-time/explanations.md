# Assignment

Python strings hide few surprises. Since scripting generally involves some form of string processing,
it is advisable to familiarize yourself with the built-in functionality.

Write a function `format_time(h, m, s)` that, given three integers `h`, `m` and `s`,
uses them to construct a string of the form `h:m:s`. All numbers must
count exactly two digits. E.g., `format_time(1,2,3)` must produce `01:02:03`, not `1:2:3`.

## Conversion to string

You will probably need to explicitly convert integers to strings.
[Google how to do this](http://lmgtfy.com/?q=python+int+to+string).

## String Interpolation

Python is strongly typed, even more so than Java.
Java allows you to build a string as follows:

```java
int h, m, s;
String result = h + ":" + m + ":" + s;
```

This code adds integers and strings together. This is allowed: all integers are
implicitly converted to string first, after which `+` performs string concatenation.

Python is stricter in this regard: strings must be added to strings, mixing
of types is disallowed. This means that you would need to write

```python
result = str(h) + ":" + str(m) + ":" + str(s)
```

This is quite cumbersome. Fortunately, there is an easier way: string interpolation.

```python
f'{h}:{m}:{s}'
```

String interpolation needs to be explicitly activated by prefixing the string
literal with an `f`. For this reason, these strings are also called *f-strings*.
In an f-string, all occurrences of `{expr}` are replaced by the value of `expr`.

## Padding Strings

For single digit numbers, you need to add leading zeros: e.g., `"5"`
must be expanded to `"05"`. Consult the [Python docs](https://docs.python.org/3/library/stdtypes.html#string-methods). Hint: `rpad`.
