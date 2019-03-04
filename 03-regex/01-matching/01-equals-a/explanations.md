# Regular Expressions

Consider the following functions:

* `is_valid_time(string)` which checks if `string` has the form `hh:mm:ss`.
* `is_valid_student_id(string)` which checks if `string` has the form `rNNNNNNN` where each `N` is a digit.
* `is_valid_email_address(string)` which checks if `string` has the form `fname.lname@subdomain.domain`.

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

## Regular Expressions in Python

In Python, regular expression functionality is provided through the [`re` module](https://docs.python.org/3/library/re.html). This module consists of many functions,
each one corresponding to a specific use of regular expressions. For now, we focus on simply checking
if a string matches a pattern.

The function `re.fullmatch(regex, string)` does exactly that: it determines whether
`string` satisfies the pattern described by `regex`. If it does, `fullmatch` returns
a truthy value, otherwise a falsey one. The only question that remains is, what does
this regex minilanguage look like? What form should `regex` take?

Let us start with a very simple pattern: we want to check whether `string`
consists of exactly one character, namely `a`. The regex expressing this pattern is
simply `a`.

In order to check if some string `string` matches a pattern described by `a`, we rely
on `fullmatch`:

```python
if re.fullmatch('a', string):
    # string does indeed match the pattern 'a'
```

## Assignment

Write a function `equals_a(string)` that checks if `string` equals
the `'a'` making use of regular expressions.
