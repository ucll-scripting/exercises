# Remaining Up-To-Date

Both the `scripting` package and the exercises can be updated during the course.
It is therefore strongly recommended to subscribe to updates.

Open both these pages:

* [`scripting` repository](https://github.com/ucll-scripting/scripting)
* [Exercises repository](https://github.com/ucll-scripting/exercises)

Press the Watch dropdown button (upper right corner) and select 'Releases only'.

Whenever you are notified of a new release, you can retrieve it by entering the command below somewhere inside the repository:

```bash
$ git pull
```

## Updating the exercises

Open a terminal inside your local copy of the exercises (any subdirectory will do) and enter the following command:

```bash
$ git pull
```

## Updating the `scripting` package

Enter the following command in a terminal (`pip3` instead of `pip` for Mac users):

```bash
$ pip install --upgrade git+https://github.com/ucll-scripting/testing-framework.git
```
