# Assignment

Python strings hide few surprises.
Scripting generally involves some form of string processing,
so it is advisable to familiarize yourself with the built-in functionality.

Translate the function below that, given three integers `h`, `m` and `s`,
uses them to construct a string of the form `h:m:s`. All numbers must
count exactly two digits. E.g., `format_time(1,2,3)` must produce `01:02:03`, not `1:2:3`.

```javascript
function formatTime(h, m, s)
{
    const hstr = `${h}`.padStart(2, '0');
    const mstr = `${m}`.padStart(2, '0');
    const sstr = `${s}`.padStart(2, '0');

    return `${hstr}:${mstr}:${sstr}`;
}
```

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
result = f'{h}:{m}:{s}'
```

String interpolation needs to be explicitly activated by prefixing the string
literal with an `f`. For this reason, these strings are also called *f-strings*.
In an f-string, all occurrences of `{expr}` are replaced by the value of `expr`.

## Padding Strings

We want each component two be exactly two digits long.
This means that single digit numbers such as `"5"` need [padding](https://lmgtfy.app/?q=python+padding+string) to turn them into `"05"`.
