# Assignment

**Note:** Install the VSCode Markdown Preview Mermaid Support extension to view the diagrams below.

Say you have written the following four scripts.

The first, `transactions.py`, contacts your bank and fetches all transactions made in the last year.
It prints out one transaction per line:

```bash
$ python transactions.py
1/1/2019 8  McDonalds
2/1/2019 12 Kinepolis
5/1/2019 35 Groceries
```

Next, you have a script `filter.py` that, given a file, prints out all lines
that contain a specific keyword.

```bash
# Shows contents of file
$ python print.py data.txt
blah blah
blah blah blah keyword blah blah blah
blah blah blah
blah keyword blah blah blah keyword blah blah
blah

# Prints lines that contain 'keyword'
$ python filter.py data.txt keyword
blah blah blah keyword blah blah blah
blah keyword blah blah blah keyword blah blah
```

Thirdly, `select.py` takes a file and a number N and prints the Nth number of each line.
Words are assumed to be separated by spaces.

```bash
$ python print.py data.txt
a b c d
1 2 3 4
xx yy zz

$ python select.py data.txt 2
b
2
yy
```

Finally, `sum.py` reads in a file containing one number per line and prints out the sum.

```bash
$ python print.py data.txt
4
2
6
7

$ python sum.py data.txt
19
```

Now, say you want to know how much you spent on groceries in total.
You can find out by combining the four scripts:

* You download your transactions.
* You keep only those transactions containing `Groceries`.
* You select the second column, as that contains the amount spent.
* You make the sum of all numbers.

Currently, all your scripts simply print out their results, i.e., they don't store them anywhere
and they are essentially lost. You somehow need to find a way to intercept whatever
data they print.

You could simply modify the scripts so that they write their results to file.
However, this is not very practical:

* We'd need to invent names for the files.
* We'd need to clean up the intermediate files.
* In case we're working with a lot of data, a lot of storage for temporary files might be required.

It'd be easier if we could somehow chain them together, to be able to tell that
the first script's output is the second script's input, etc.

<center>

```mermaid
graph LR;
    transactions.py-->filter
    filter-->select;
    select-->sum;
```

</center>

## Streams

A *stream* is an abstracted view of a data source or receiver. Let's clarify this
with some examples:

* A keyboard can be seen as a data source: each key the user types is a
piece of data.
* A keyboard (a regular one at least) is not a data receiver: what would it mean
to send data to a keyboard? Would sending an `A` have its key go down?
* A mouse is, like a keyboard, a data source: mouse movements and clicks form the data.
* A microphone is a data source.
* A screen is a data receiver: data represents pixels of different colors.
* Speakers are data receivers: they transform bits into sound.
* Files can act both as data sources and data receivers.

An *input stream* is basically something you can read data from.
You can imagine it as a very limited object with just one operation, `read`,
which returns the next piece of data.

An *output stream* is something you can write data to.
It supports only one operation: `write`.

Some things, such as files, combine both types of streams:
one can both read and write from files, so they can act
as both input and output streams.

Whenever you open a file or make an http request, you get
a stream with which to interact:

```python
with open(filename, 'r') as input_stream:
    input_stream.read()   # Reads data from file

with open(filename, 'w') as output_stream:
    output_stream.write(data)   # Writes data to file
```

## Standard Streams

Whenever you start a new process (e.g. when you run a Python script or launch a game),
it receives three premade streams from the OS, the so-called *standard streams*:

* STDIN or the standard input stream.
* STDOUT or the standard output stream. When you print using `print` (or `System.out.println` in Java), this is the stream where your data goes to.
* STDERR or the standard error stream.

What these streams correspond to, depends on the context.
If you start a process from the shell, STDIN is connected to the keyboard
and everything written to STDOUT and STDERR is shown in the console.

<center>

```mermaid
graph LR
    xxx -- STDIN -->process
    process-- STDOUT -->display
    process-- STDERR -->display
```

</center>

GUI applications also have standard streams, but generally,
they are not attached to anything.

<center>

```mermaid
graph LR
    in["nothing"]
    out["nothing"]
    in -- STDIN -->process
    process-- STDOUT --> out
    process-- STDERR --> out
```

</center>

These standard stream connections can be freely redirected as you see fit.
For example, IDEs generally redirect whatever is written to STDOUT and STDERR
to a separate window pane. This can be useful for debugging:
say you are developing a GUI application, you can then print diagnostic
messages to either STDOUT or STDERR. If run from within an IDE,
these messages will appear in a specifically designated window. If run normally,
the diagnostic messages will simply be ignored.

<center>

```mermaid
graph LR
    in["nothing"]
    out["IDE"]
    in -- STDIN -->process
    process-- STDOUT --> out
    process-- STDERR --> out
```

</center>

## Piping

We can solve our original problem by redirecting the standard streams ourselves.
Say we adapt our scripts `filter.py`, `select.py` and `sum.py` so that
instead of reading their data from a file, they read it from STDIN:

```python
with open(filename, 'r') as input_stream:
    input_stream.read()

# becomes

sys.stdin.read()
```

This allows us to chain scripts together:

* `transactions.py` simply prints out the transactions, i.e., to STDOUT.
* `filter.py` receives its data from STDIN and prints its output to STDOUT.
* `select.py`: similarly.
* `sum.py`: similarly.

To attach one script's STDOUT to the next one's STDIN, we can use piping:

```bash
$ python transactions.py | python filter.py Groceries | python select.py 2 | python sum.py
```

## Advantages

Instead of having four scripts and pipe them together, we could have
simply written one script that combines the functionality. However,
this would make reusing the parts impossible: filtering, selecting
and summating are operations that can be used in other contexts.

Each script can also be written in a different language.
Say there is a tool that implements functionality
that you need, but it's written in, say, Go. There's
no simple way to call Go functions directly from Python.
However, by relying on the shell you can have
to Go program output its result to STDOUT and redirect it to your Python
script.

The shell also offers you interactivity: you can combine
your scripts incrementally, checking your results
at each step. It is important that you do not try
to build something in one go: check as often as you can.

## Disadvantages

Generally, the shell is used for single-use programs.
If you need to compute the total amount spent
on groceries regularly, you will want to
store your shell command in a file, a *shell script*:

```sh
# File sum-groceries.sh
#!/usr/bin/env bash

python transactions.py | python filter.py Groceries | python select.py 2 | python sum.py
```

However, this will quickly lead you to a path where you start implementing nontrivial
logic in the shell itself. While programming directly in the shell
is certainly a possibility (e.g., it does support conditionals and loops),
we advice against it:

* Most shells have truly *awful* programming languages. Don't be fooled by anyone purporting that "it's not programming, it's scripting, that makes it okay." If you are writing nontrivial logic and bugs are unwelcome, it does not matter whether you call it programming or scripting.

* Scripts written in different languages can communicate because data is encoded as strings. This is actually incredibly inefficient. For example, each time a numeric value needs to be transferred, it must be converted to a string, only to be parsed again into a number. If you remain within the same language, no such translations are necessary.

What's best mostly depends on your actual needs. There are many aspects to take into consideration:

* There are many shells. Not all shells are available on all platforms. Does your script need to be run on other platforms, or only on your own?
* Some shells do not make use of strings to transfer data. For example, Powershell allows integers, booleans, even entire objects to retain their structure, which makes it a lot more efficient and safer.
* You can start off with shell scripts and replace them with scripts written in more robust languages if need be.

## Task

Write a script that reads STDIN and counts the number of lines of code.

To read from STDIN, you can use `input()`, which returns one line. You can also take a look at `sys.stdin`, as this object offers you more methods,
which may help you write simpler code.

By default, empty lines (or lines with only whitespace) are ignored. Using the `-e` or `--count-empty-lines` flag leads them to be counted.

The `--comment=STRING` option lets you specify how comments are introduced, e.g., `#` for Python or `//` for Java. When
specified, lines containing only comments will also be ignored.

Since your script takes its input from STDIN, you need to have a way to feed it data through STDIN.
One approach would be to use a different script that given a filename prints its output to STDOUT, so that
you can chain them

```bash
$ python print.py input-file | python loc.py
```

You can also rely on `cat`, which does the same as `print.py`:

```bash
$ cat input-file | python loc.py
```

You can also use the built-in `<` shell operator:

```bash
$ python loc.py < input-file
```