# Assignment

Generate the following table:

```text
         0                 0b0       0x0
         1                 0b1       0x1
         2                0b10       0x2
         3                0b11       0x3
         4               0b100       0x4
         5               0b101       0x5
         6               0b110       0x6
         7               0b111       0x7
         8              0b1000       0x8
         9              0b1001       0x9
        10              0b1010       0xa
```

Instead of stopping at 10, the table should go up to 10000.

* The first column must be 10 characters wide.
* The second column must be 20 characters wide.
* The third column must be 10 characters wide.

```text
    10             20              10
|--------|--------------------|----------|
         0                  0b0        0x0
```

## Hints

* Look up how to convert a number to hexadecimal and binary.
* The `rjust` method of strings could help you out.
