# Assignment

Write a function `make_path(parts)` that, given an array of strings,
builds a path out of them by joining them together in one large string,
separated by slashes.

For example, say `parts = ['a', 'b', 'c']`, `make_path(parts)`
should then return `'a/b/c'`.

```javascript
function makePath(parts)
{
    return parts.join('/');
}
```
