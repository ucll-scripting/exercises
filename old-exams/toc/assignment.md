# Assignment

You are given as AsciiDoc file for which you need to create a table of contents.

First, you will need to find all section headings.
A heading is a line that starts with one or more `=` symbols, followed by a space, followed by a title.
The number of `=` symbols represents the level of the section.
On the line _before_ the heading, its id is defined using the syntax `[#id]`.

```text
[#main]
= Title

Some text

[#sub]
== Subtitle

Some more text.
Lorem ipsum and stuff.

[#subsub]
=== Subsubtitle

Text.
```

In the example above, there are three headings:

* The first one has title `Title` and id `main`. It has level 1.
* The second one has title `Subtitle` and id `sub`. It has level 2.
* The third one has title `Subsubtitle` and id `subsub`. It has level 3.

From this, you need to create a table of contents as a bullet point list with links to the corresponding heading.
The structure of the bullet point list must mirror that of the entire document: a level N heading must be represented by a bullet point with "depth" N.

```text
* <<main,Title>>
** <<sub,Subtitle>>
*** <<subsub,Subsubtitle>>
```

Note the following:

* A bullet point of depth K starts with K `*` symbols.
* A link is written `<<id,title>>`. Note that you must not add a comma after the space.

Write this table of contents to a file named `output.txt`.
