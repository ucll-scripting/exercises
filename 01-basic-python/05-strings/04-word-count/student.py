# Write your code here
"""# Assignment

Write a function `word_count(string)` that counts the number of words in `string`.
You can make the assumption that words are simply separated by a single space.
You can ignore punctuation.

```javascript
function wordCount(string)
{
    return string.split(' ').length;
}
```
"""
def word_count(string):
    return len(string.split())
