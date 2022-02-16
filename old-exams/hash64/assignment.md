# Assignment

## Quick Background

The information in this section is not important to solve the exercise.
It is merely provided for context.

SHA384 is a _secure hash algorithm_.
It takes input and then "hashes" this into a single number.
This number is 384 bits long, so it is quite large, which is why Python represents the hash value as an array of 48 bytes.

Base64 is a way of representing numbers.
You are used to decimal notation, which uses 10 digits, meaning it is base 10.
Binary has two digits, so it is base 2.
Base64 simply uses 64 different digits.

## Your Task

For each integer `I` going from 0 to 10000 (included), compute the SHA384 value and encode the hash in base64.
Write your results in a file where each line contains the integer I followed by a space, followed by its hash value:

```text
I HASH
```

## Details

* The Python standard library contains functions that compute the SHA384 and base64 encoding for you.
* In order to compute the SHA384 of an integer `I`:
  * Convert `I` to a string.
  * Convert this string to raw bytes using `encode`. Use `ascii` as encoding.
  * Give these raw bytes to the SHA384 function.
* The base64 function returns raw bytes.
  In order to print this, you need to convert these to a regular string.
  Rely on the `decode` method. Again use `ascii` as encoding.

## Example

We consider here `I` = 0.

* We convert it to a string, which gives us `'0'`.
* We convert this to raw bytes using ascii encoding, which, which Python will show as `b'0'`.
* We hash this using SHA384, which gives us the following byte array (48 long):

```text
b'_\x91U\x0e\xdb\x03\xf0\xbb\x89\x17\xdaW\xf0\xf8\x81\x89v\xf5\xda\x97\x13\x07\xb7\xeeH\x86\xbb\x95\x1cH\x91\xa1\xf1o\x84\r\xae\x8feZ\xa5\xdfq\x88\x84\xeb\xc1['
```

* We convert this to base64, yielding another byte array:

```text
b'X5FVDtsD8LuJF9pX8PiBiXb12pcTB7fuSIa7lRxIkaHxb4QNro9lWqXfcYiE68Fb'
```

* Finally, transforming this into a string using ascii gives

```text
'X5FVDtsD8LuJF9pX8PiBiXb12pcTB7fuSIa7lRxIkaHxb4QNro9lWqXfcYiE68Fb'
```

In other words, the first line of `output.txt` should be

```text
0 X5FVDtsD8LuJF9pX8PiBiXb12pcTB7fuSIa7lRxIkaHxb4QNro9lWqXfcYiE68Fb
```

To help you check your work, here are the first five lines of `output.txt`:

```text
0 X5FVDtsD8LuJF9pX8PiBiXb12pcTB7fuSIa7lRxIkaHxb4QNro9lWqXfcYiE68Fb
1 R/BdNnsMMuQ4+2Pmz0pfNcKqL5DcdUP4pBoPlc6KQKMTq1zzYTSiBoxMlpy1Dbd2
2 0GNFdwXWbW8BbkzddH2zr41w6/02ut1j3myMpKnYv7XYdOf711CqgE3K3a5+7vUe
3 avEcg1hoIsPHS7PM73KLrlz+5nytgt10AnEeUwvseC/AKv8nNWnSLd/7OxRfNDdo
4 vPbg68jFGFNyyNjw9Elye9UsUoSGDxxG6lPclD+r9Ax1BnYpgT8SvZlNdaOfRIQ9
```
