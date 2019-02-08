# Scripting Exercise Repository

## Installation

Install the following software:

* [git](https://git-scm.com/)
* [Python](https://www.python.org/downloads/)
* [Visual Studio Code](https://code.visualstudio.com/)

Open a terminal in a directory where you wish to store your files.
Enter the commands below. **Always omit the `$`!** It is conventional to prefix
lines with commands you are expected to enter with `$`.

```bash
$ pip install git+https://github.com/UCLeuvenLimburg/scripting.git

$ git clone https://github.com/UCLeuvenLimburg/scripting-exercises.git
```

Test the installation of the scripting package by executing the following command.
It should show the output below (or something similar to it, as long as it's not an error message.)

```
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
