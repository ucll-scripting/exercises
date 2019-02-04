# Regular Expressions

Consider the following functions:

* `is_valid_time(string)` whichs check if `string` has the form `hh:mm:ss`.
* `is_valid_email_address(string)` whichs check if `string` has the form `fname.lname@subdomain.domain`.
* `is_valid_student_id(string)` which checks if `string` has the forn `rNNNNNNN` where each `N` is a digit.

Each of these performs the same job: check if the given string satisfies a certain pattern.
This kind of functionality occurs often (e.g. user input validation). While it is certainly
possible to write algorithms that perform these tasks, it is quite arduous and bug prone to do so.

Regular expressions (regexes for short) were developed to simplify implementing pattern checking algorithms:
these are a minilanguage highly specialized in succinctly describing patterns.

Regular expressions are not specific for Python: almost all languages
have support for them.

* Java: the [`Pattern`](https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html) class.
* JavaScript: regexes built into the language.
* C#: the [`Regex`](https://docs.microsoft.com/en-us/dotnet/api/system.text.regularexpressions.regex) class.

# Regular Expressions in Python

In Python, regular expression functionality is provided through the [`re` module](https://docs.python.org/3/library/re.html). This module consists of many functions,
each one corresponding to a specific use of regular expressions. For now, we focus on simply checking
if a string matches a pattern.

The function `re.fullmatch(regex, string)` does exactly that: it determines whether
`string` satisfies the pattern described by `regex`. The only question that remains is, what does
this regex minilanguage look like? What form should `regex` take?

Let us start with a very simple pattern: we want to check whether `string`
consists of exactly one character, namely `a`.


# Assignment

Write a function `equals_a(string)` that checks if `string` equals
the `'a'`.

You could of course write

```python
def equals_a(string):
    return string == 'a'
```

This is by far the most straightforward and efficient solution. However,
our intention is to start using regular expressions.
