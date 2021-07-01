# Assignment

Take a look at the contents of `input.txt`.
Each line contains a name, followed by an IP address and a country.
Write a script that formats the contents into a nice table.
The result should be written to a file named `output.txt`.

It's important to get the formatting exactly right.
Below we list the rules.

```text
             name ip       country
|               | |      |
<---------------> <------>
       W1            W2
```

* There should be three columns.
  * The first column must contain the name.
  * The second column must contain the ip address.
  * The third column must contain the country.
* Each column should be just wide enough to accommodate its largest content.
  * W1 should be equal to the length of the longest name.
  * W2 should be equal to the length of the longest IP address.
  * The last column does not need padding to make it a certain width. In other words, there should be no trailing spaces.
* Columns should be separated by a single space.
* The first column should be right aligned, whereas the second and third column should be left aligned.
* Only spaces are allowed to align the text. Do not rely on tabs.
* The order in which the rows appear should be the same as in the input file.

## Example

Say `input.txt` contains

```text
Sydney Clark 106.37.136.123 British Virgin Islands
Kristin Schwartz 147.202.106.81 Iceland
Steven Watkins 84.35.112.148 Brazil
Jeff Hill 74.102.135.229 Slovenia
Mr. Jesse Simpson DDS 182.157.226.16 Thailand
```

This should be reformatted as

```text
         Sydney Clark 106.37.136.123 British Virgin Islands
     Kristin Schwartz 147.202.106.81 Iceland
       Steven Watkins 84.35.112.148  Brazil
            Jeff Hill 74.102.135.229 Slovenia
Mr. Jesse Simpson DDS 182.157.226.16 Thailand
```
