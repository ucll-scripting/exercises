# Assignment

Regular expressions can also be used to perform substitutions in text:
you can ask any substring that matches a certain pattern
to be replaced according to some rules. This functionality
is embodied by the `sub` function in the `re` module.

Let's start with something relatively simple.

Are you one of those people who can't stand useless whitespace
at the end of lines in your code? Do you maniacally
remove it whenever you notice it? Did you perhaps
even look for an option in your editor to automatically
remove that trailing whitespace (because there is one in Visual Studio Code, you know.)
Good news, everyone! This exercise will let you write a function `remove_trailing_whitespace` that hunts down those horrible
utterly useless spaces and shreds them to nothingness.

`sub` takes three parameters:

* A regex
* A replacement string
* The string in which to perform the substitutions

Let's find out which values to pass to `sub`.

The third parameter is easy: it's whatever string `remove_trailing_whitespace` receives.
The second parameter is not too difficult either: since we want
to make something disappear, the replacement string should simply be `''`.

Lastly, the regex. We need a pattern that matches trailing whitespace, i.e.,
spaces that appear at the end of a line. We'll let you look for the answers
to this riddle in the [documentation](https://docs.python.org/3/library/re.html).
Hints: there is a special character that matches the end of lines, but you
need to turn on multiline mode.
