# Assignment

You are grading a multiple choice quiz.
Given the correct answers and the students' answers, you need to count how many questions each student answered correctly.

The file `solutions.csv` contains the correct answers to the quiz as a single line of comma separated letters.

The file `answers.csv` contain the students' answers.
Each line is a list of comma separated values:

* The first value represents the student's name.
* The remaining values represent that student's answers to the quiz.

Produce a file `output.txt` which contains the students' scores.

* Each line corresponds to a single student.
* A line contains the student's name followed by his/her score. This score is equal to the number of correct answers.
* The students must appear in the same order as in `answers.csv`.

# Example

Say the quiz counts 5 questions and `solutions.csv` contains

```text
c,a,a,b,e
```

Say `answers.csv` contains

```text
John Doe,c,e,a,b,e
Jane Doe,a,a,a,a,a
```

* John Doe has answered all questions correctly except for the second one. His score is 4.
* Jane Doe only answered two questions correctly, hence her score is 2.

Your script must therefore generate the following `output.txt`:

```text
John Doe 4
Jane Doe 2
```
