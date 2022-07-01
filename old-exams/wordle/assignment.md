# Assignment

## Background

Wordle is a game where you have to guess a secret word consisting of 5 letters.
For this, you get six guesses.
After each guess, you get feedback

* A letter can be correct at the right position (`C`).
* A letter can be correct but misplaced (`M`).
* A letter can be wrong in the sense that it does not occur anywhere in the secret word (`W`).

For example, say that the secret word is `ports`.

* At first you don't know anything about the word except its length (5 letters).
* Your first guess is `steak`.
  The feedback you receive is `MMWWW`, which means
  * The first letter of your guess (`s`) does appear in the secret word, but not in the first position.
  * The second letter of your guess (`t`) also appears in the secret word, but not in the second position.
  * The third, fourth and fifth letters (`e`, `a` and `k`) do not appear at all in the secret word.
* Your second guess is `tolls`.
  The feedback is now `MCWWC`, which means
  * The `t` appears in the secret word, but not in the first position.
  * The `o` is correctly placed: the secret word does have an `o` as its second letter.
  * The secret word does not contain an `l`.
  * The secret word ends on a `s`.

In summary, given the feedback on these two guesses, you know that

* The secret word has the form `.o..s`.
* A `t` must appear somewhere, but not at the first or second position.
* The letters `e`, `a`, `k` and `l` do not occur in the secret word.

## Your Task

You get a list of words (`words.txt`) in alphabetical order.
We are using 8-letter words instead of 5-letter words.
The secret word is one of the words appearing in `words.txt`.

Next, we give you two guesses and their feedback:

* `abcdefgh` gives as feedback `MMMMWWWW`.
* `xxxxxxxx` gives as feedback `WWWWCWWW`.

Put differently,

* The letters `a`, `b`, `c`, `d` do appear in the secret word, but not at those positions.
* The `x` does appear exactly once and its location is known.
* No `e`, `f`, `g` or `h` occurs in the secret word.

This information is not enough to uniquely determine the secret word: six words from `words.txt` are compatible with these constraints.
Determine these six words and write them to `output.txt`, in alphabetical order.

Hint: you can rely on `words.txt` already containing words in alphabetical order.
