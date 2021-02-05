# Installation

## Software

Install the following software:

* [Git](https://git-scm.com/)
* [Python 3](https://www.python.org/downloads/)
  * During the installation, don't forget to have Python added to environment variables (!)
  * Also double check that pip is selected as optional feature as well
* [Visual Studio Code](https://code.visualstudio.com/)
  * Windows users: during the installation, have it install the explorer context menu additions
  * Install the VSCode Markdown Preview Mermaid extension.

## Checking Your Python Installation

It's important to check that your Python installation works.
This can be slightly tricky, since the details depend on your OS.
There are two kinds of problems that can arise:

* Python cannot be found
* The wrong version of Python is found

Below are instructions that verify both at the same type.
The goal is that you get Python to tell you which version it is, and that this version is 3.6 or higher.
If you encounter problems, inform a lecturer.

IMPORTANT: a `$` in the beginning of a line means that you should input that line in a shell.
**Do not write the `$` itself though, only what follows**. For example, `$ ls` means you should enter `ls`.
Similary, a `#` represents comments, so these can be omitted altogether.

### Windows

In a shell, write

```bash
$ python --version
```

If this gives you trouble, try instead

```bash
$ py --version
```

### Mac

In the terminal, write

```bash
$ python --version
```

If this doesn't work or prints out the wrong version, try

```bash
$ python3 --version
```

### Linux

In a shell, write

```bash
$ python --version
```

If this doesn't work or prints out the wrong version, try

```bash
$ python3 --version
```

## Checking Your Pip Installation

Pip is Python's package manager: it allows you to easily install now components.
Check if it works by trying out the commands below:

```bash
$ pip --version

$ pip3 --version
```

One of these should work and should output something mentioning Python 3.
If this isn't the case, inform a lecturer.

## Course Related Material

Next, open a terminal in a directory where you wish to store your course-related files.
Enter the commands below.

```bash
$ pip install git+https://github.com/ucll-scripting/testing-framework.git

$ git clone https://github.com/ucll-scripting/exercises.git
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
