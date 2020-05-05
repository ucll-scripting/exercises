# Assignment

We're writing a text containing many numbers written in hexadecimal.
Since it's a bit tiresome to always manually convert
from decimal to hexadecimal, we decide to automate the process.

Say we wish the value 421 to appear in hexadecimal.
Instead of opening up some calculator and have it comvert the
value to `0x1A5`, we simply write `$HEX(421)`. A script
will then go over the text and replace every instance
of `$HEX(value)` with the hexadecimal form of `value`.

Open `input.txt`, look for all occurrences of `$HEX(value)`,
replace them with hexadecimal notation and write the results to `output.txt`.

## Example

Say the file `input.txt` contains the following data:

```text
fdlksfsdlj $HEX(128) fjkaljfl kjlq $HEX(65535).
qjdijd $HEX(0) jflkjflkj $HEX(111)
```

`output.txt` should then contain

```text
fdlksfsdlj 0x80 fjkaljfl kjlq 0xFFFF.
qjdijd 0x0 jflkjflkj 0x6F
```

Make sure the letters `A`, `B`, `C`, `D`, `E`, `F` appear in uppercase,
i.e., `0x5A2B` is correct, but not `0x5a2b`. Note that the `x` is still lowercase.
