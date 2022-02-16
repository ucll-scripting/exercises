# Assignment

You are probably familiar with HTML: it is a markup language, which allows you to define the structure of a text.
HTML, however, is quite verbose and not very human-friendly.
Markdown and AsciiDoc are markup languages that are more lightweight and easier to use than HTML.

Your task will be to convert a Markdown file into an equivalent AsciiDoc file.
A full translation would take a lot of time, so we focus on just two things.

## Section Headings

HTML uses `<h1>...</h1>`, `<h2>...<h2>`, etc. to denote headings of different levels.
Markdown uses the more lightweight syntax `# ...` and `## ...`: the number of `#` symbols indicates how "deep" the heading is.
AsciiDoc works exactly the same, except it uses `=` symbols instead of `#`.

The first part of your job is to look for all lines starting with on or more `#` symbols and replace these by `=`.
Note that the `#` has to be placed at the _very beginning_ of the line, otherwise it needs to be ignored.

## Bullet Point Lists

In Markdown, bullet lists are written

```text
* Level 1 item
* Second level 1 item
  * Subitem (level 2)
    * Subsubitem (level 3)
  * Another subitem (level 2)
```

As you can see, bullet point lists can be recognized by their `*` symbols.
Sublists are indented using _exactly_ two spaces per level, i.e., a subsubitem will start with 4 spaces, then an asterisk, then the title.

In AsciiDoc, the same list is written

```text
* Level 1 item
* Second level 1 item
** Subitem (level 2)
*** Subsubitem (level 3)
** Another subitem (level 2)
```

Instead of using indentation, AsciiDoc simply increases the number of `*`s to denote the depth.

## Your Task

Translate the given `input.md` file to `output.txt`:

* Translate all section headings.
* Translate all bullet lists.

All other content must be kept unmodified.

## Example

Consider the following Markdown file:

```text
# Title
Some paragraph text

## Subtitle 1
Text.
More text.

## Subtitle 2

### Subsubtitle

Let's make a nice list.

* First item
* Second item
* Third item
  * Subitem
  * Another subitem
* Fourth item
  * Deeper we go
    * Even deeper
      * Very deep

## Something else entirely
Last line.
```

It must be translated to

```text
= Title
Some paragraph text

== Subtitle 1
Text.
More text.

== Subtitle 2

=== Subsubtitle

Let's make a nice list.

* First item
* Second item
* Third item
** Subitem
** Another subitem
* Fourth item
** Deeper we go
*** Even deeper
**** Very deep

== Something else entirely
Last line.
```
