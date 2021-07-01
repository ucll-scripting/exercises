# Assignment

You want to hack into your mortal enemy's account.
For this, you intend to try out every possible password in turn.
However, you have observed him for a long time and have found out a few crucial bits of information about his password.

* His password consists of exactly 6 characters.
* This password only uses the top row letter keys on a qwerty keyboard: `QWERTYUIOP`.
* All letters are in uppercase.
* The password contains twice the same vowel in a row (for example, `PEEQOP`: the vowel `E` appears twice in a row).
  Vowels are `AEIOU`; we do not count `Y` as a vowel.
* Similarly, the password contains twice the same consonant in a row (e.g. `PORRQO` contains the consonant `R` twice in a row).
* Apart from the two vowels and two consonants mentioned above, there are no duplicate letters.
  In other words, after removing all duplicates, there should be 4 letters left in the password.

Produce a list of all possible passwords that satisfy these conditions.
Write this list in alphabetical order to a file named `output.txt`.

## Hints

* Generating all passwords using the given letters is easy as there exists a function in Python's standard library that does exactly that. It has been used in one of the exercise.
* Go through all possible passwords and print out only those that satisfy the conditions.
* No complex algorithmic code is necessary.
* Hint: regex backreferences might come in handy.

## Examples

`EEIOPP` is one of the possible passwords:

* It consists solely of uppercase letters made from the top row keys.
* It has length 6.
* It contains the vowel `E` twice in a row.
* It contains the consonant `P` twice in a row.
* It contains four distinct letters `E`, `I`, `O` and `P`.
