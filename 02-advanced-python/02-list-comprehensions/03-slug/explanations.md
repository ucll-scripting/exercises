# Assignment

We have a of name (of a person) and wish to derive a [slug](https://en.wikipedia.org/wiki/Clean_URL#Slug) from it.
For example, the slug for `John Johnson` is `johnson-john`. The rules regarding slugs are

* All letters are in lowercase.
* The slug contains the last name followed by the first name.
* Spaces are replaced by dashes.

Some names consist of three 'words', e.g., `Simon Peyton Jones`. In
these cases, you should assume that the first name
corresponds to the first word and the remaining words together
form the last name. This results in the slug `peyton-jones-simon`.

Some other examples:

* 'Prince' results in slug `prince`
* 'Dennis Ritchie' results in slug `ritchie-dennis`
* 'Guido van Rossum' results in slug `van-rossum-guido`
* 'John Wilkes Booth' results in slug `wilkes-booth-john`

Suggested approach:

* First, look for a way to split a string into "words", for example, `"abc def gh"` should be split into `['abc', 'def', 'gh']`.
  This functionality is built-in, so do NOT implement it yourself.
* Find a way to convert a string into lowercase.
* Use a list comprehension to convert all strings from the first step into lowercase.
* Join these strings together using built-in functionality.
