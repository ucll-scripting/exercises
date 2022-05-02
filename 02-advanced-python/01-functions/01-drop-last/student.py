# Write your code here
"""Let's generalize `drop_last`. In a previous exercise, you
had to write `drop_last(xs)` which dropped the last element
of `xs`. But maybe you want to drop the last *two* elements.
Or the *three* last. So, you decide to add an extra parameter:
`drop_last(xs, n)` where `n` indicates how many elements
have to be dropped.

Adding an extra parameter to `drop_last` causes some problems:"""
def drop_last(xs,n=1):
    return xs[:-n]
