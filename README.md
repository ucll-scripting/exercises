# Scripting Exercise Repository

## About This Course

This course teaches you how to write small scripts that automate tasks.
For this, we will rely on the Python programming language:

* It is one of the most used programming languages (see [Tiobe](https://www.tiobe.com/tiobe-index/), [StackOverflow](https://insights.stackoverflow.com/survey/2018#most-popular-technologies), [GitHub](https://octoverse.github.com/projects#languages)).
* It is one of the most user-friendly languages out there.
* A very large number of packages are available, which is essential for scripting.

The focus lies on *getting things done*. Your scripts have to produce
correct results and it is your responsibility to check your work properly.
The first series of exercises are accompanied by tests,
but with the 'real deal' exercises, that won't be the case anymore.
You will have to split up the task at hand in smaller pieces,
implement helper functions, check them, etc.

We do not care *how* you solve the problem. You are free
to use all of the functionality Python provides. It is not our
goal to have you write complex algorithms. So, please
do not write your own `sum` function, use the built-in one.
You will see that Python has *a lot* of built-in functions
for you to make use of. Therefore, it is very important
that you develop the habit of skimming through the documentation
and looking up information online.

## Installation

### Software

Install the following software:

* [Git](https://git-scm.com/)
* [Python 3](https://www.python.org/downloads/)
  * During the installation, don't forget to have Python added to environment variables (!)
  * Also double check that pip is selected as optional feature as well
* [Visual Studio Code](https://code.visualstudio.com/)
  * Windows users: during the installation, have it install the explorer context menu additions
  * Install the VSCode Markdown Preview Mermaid extension.

Make sure to check your Python version as follows (this is especially
important for Mac and Linux users). Open a terminal and input the following command.
(**Omit the `$`!** It is conventional to prefix
lines with commands you are expected to enter with `$`.)

```bash
$ python --version
```

This should respond with the installed Python version. You need at least 3.6.
If it responds with some 2.x version, you're probably a Mac user. Try again with

```bash
$ python3 --version
```

If you get an error or the wrong version, inform a lecturer.

### Course Related Material

Next, open a terminal in a directory where you wish to store your course-related files.
Enter the commands below.
If the pip command does not work, look online for 'how to install pip'.

**Windows Users**
```bash
$ pip install git+https://github.com/UCLeuvenLimburg/scripting.git

$ git clone https://github.com/UCLeuvenLimburg/scripting-exercises.git
```

**Mac Users**
```bash
$ pip3 install git+https://github.com/UCLeuvenLimburg/scripting.git

$ git clone https://github.com/UCLeuvenLimburg/scripting-exercises.git
```

Test the installation of the scripting package by executing the following command.
It should show the output below (or something similar to it, as long as it's not an error message.)

```bash
$ scripting
usage: scripting [-h] {version,test} ...

positional arguments:
  {version,test}  sub-command help
    version       returns version
    test          runs tests in all subdirectories

optional arguments:
  -h, --help      show this help message and exit
```

## Usage

Use Visual Studio Code to open the `scripting-exercise` folder. Under Windows, this can be done by right-clicking the folder and choose 'Open with Code'. This way, the side bar gives a nicely structured view of all the exercises.

Each exercise is stored in its own folder. This folder contains a number of files:

* `explanations.md`: your starting point. It is strongly recommended you read through it, as it contains important information about the exercise.
* `student.py`: write your solutions here.
* `tests.py`: contains the tests. In some cases it might be useful to take a look at this.
* `solutions.py`: contains the solution.

To check your solution:

```bash
$ scripting test
```

This will run all tests in the current directory and all subdirectories. Generally, you will want to perform this command inside an exercise's directory, but run tests of many exercises at once, you can also execute it in a parent directory.

## Remaining Up-To-Date

Both the `scripting` package and the exercises can be updated
during the course. It is therefore strongly recommended
to subscribe to updates.

Open both these pages:

* [`scripting` repository](https://github.com/UCLeuvenLimburg/scripting)
* [Exercises repository](https://github.com/UCLeuvenLimburg/scripting-exercises)

Press the Watch dropdown button (upper right corner)
and select 'Releases only'.

Whenever you are notified of a new release, you can retrieve
it by entering the command below somewhere inside the repository:

```bash
$ git pull
```

### Updating the `scripting` package

Enter the following command in a terminal (`pip3` for Mac users):

```bash
$ pip install --upgrade git+https://github.com/UCLeuvenLimburg/scripting.git
```

### Updating the exercises

Open a terminal inside your local copy of the exercises (any subdirectory will do)
and enter the following command:

```bash
$ git pull
```


## Other Useful Shell Commands

Entering a subdirectory

```bash
$ cd subdirectory
```

Go up a directory

```bash
$ cd ..
```

View contents of current directory

```bash
$ ls
```

Open a file from the shell

```bash
$ code filename
```

## Overview of some example libraries used in the more challenging exercises

After exercise sets 01, 02, 03 and 04, we provide you with a set of more challenging exercises. To give you an idea about some of the libraries used, here's an overview. The idea is that you chose yourself what interests and/or challenges you.

```bash
backup
  zipfile
  datetime
  argparse
  sys
  os

exam schedule
  sys
  csv
  argparse

ical
  datetime
  ics
  sys
  re

imdb
  pandas
  csv
  sys

scraping
  urllib
  re

shell tools
  sys
  re
  os
  argparse

toledo unpack
  zipfile
  sys
  re
  os
```
