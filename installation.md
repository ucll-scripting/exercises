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

Make sure to check your Python version as follows (this is especially important for Mac and Linux users).
Open a terminal and input the following command.
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

## Course Related Material

Next, open a terminal in a directory where you wish to store your course-related files.
Enter the commands below.
If the pip command does not work, look online for 'how to install pip'.

**Windows Users**
```bash
$ pip install git+https://github.com/ucll-scripting/testing-framework.git

$ git clone https://github.com/ucll-scripting/exercises.git
```

**Mac Users**
```bash
$ pip3 install git+https://github.com/ucll-scripting/testing-framework.git

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