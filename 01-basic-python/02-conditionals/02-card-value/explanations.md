# Assignment

Write a function `card_value(string)` that determines the value of the card.

| Card | Value |
| ---- | ----- |
| 2 - 10 | 2 - 10 |
| Jack | 11    |
| Queen| 12    |
| King | 13    |
| Ace  | 1     |

```javascript
// Note that Python and JavaScript have different naming conventions (https://www.python.org/dev/peps/pep-0008/#function-and-variable-names)
// In Python you should name this function card_value instead of cardValue
function cardValue(string)
{
    if ( string === 'Jack' )
    {
        return 11;
    }
    else if ( string === 'Queen' )
    {
        return 12;
    }
    else if ( string === 'King' )
    {
        return 13;
    }
    else if ( string === 'Ace' )
    {
        return 1;
    }
    else
    {
        // Converts string to integer
        return parseInt(string);
    }
}
```

Look up how to [convert a string to an integer](https://lmgtfy.app/?q=python+string+to+int).
