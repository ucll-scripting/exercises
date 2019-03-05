# Assignment

Write a function `contains_a(string)` that checks whether `string` contains an `a`.
You can achieve using the regex `.*a.*`. However, let's do it a bit differently.

Until now, you've always used the `re.fullmatch(regex, string)` function. This function
demands that the *entire* string satisfies the pattern described by `regex`.
In general, however, this is not how regexes behave.

Take a look at regexes in other languages:

```java
// Java
Pattern.matches(regex, string)
```

```csharp
// C#
new Regex(regex).IsMatch(string)
```

```ruby
# Ruby
/regex/ =~ string
```

```javascript
// JavaScript
/regex/.exec(string)
```

All these implementations differ from `re.fullmatch` in that they
only expect a *substring* of `string` to satisfy the pattern.

For example, consider the regex `a`. In Python, `re.fullmatch('a', string)`
only returns a truthy value if `string` equals `a`, because `fullmatch`
requires the *entire* string to be described. In other words, `re.fullmatch('a', 'bab')` is not a match.

In the other languages, however, matching the regex `a` with the string `bab` will succeed since the regex will be interpreted as "There is a substring of `bab` that matches the regex `a`." It is important you are aware of this distinction to avoid unpleasant surprises in the future.

Now, is there a way to make Python behave like the other languages? There sure is!
Simply use `re.search` instead of `re.fullmatch`. In essence, `re.search(regex, string)` is the same as `re.fullmatch('.*regex.*', string)`.

Make use of `re.search` to solve this exercise.
