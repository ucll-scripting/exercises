# Usage

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

This will run all tests in the current directory and all subdirectories. Generally, you will want to perform this command inside an exercise's directory, but to run tests of many exercises at once, you can also execute it in one of the parent directories.
