# Assignment

Write a function `parse_link(string)` that receives an html `a`-element `<a href="...">...</a>`,
extract the link and caption from it and returns it as a tuple `(caption, link)`.

If `string` is not a well-formed `a` element, it should return `None`.