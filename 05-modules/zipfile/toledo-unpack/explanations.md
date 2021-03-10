# Explanations

Toledo offers assignments where students have to upload a file.
Us lecturers can download the student submissions as one zip.
You'd think there'd be an easy way to find out which submission belonged to which student.
But this is Toledo were talking about.

It turns out that students not only have an `r`-number (or `s`-number) but also a `q`-number.
Rumor has it that some students accidentally got assigned the same `r`-number; this problem was solved by introducing a new `q`-number behind the scenes, so that they could assign a unique id to each student.
Do not be surprised if in the near future you learn that you also have a `p`-number.

Anyway, back to our Toledo submissions.
When a lecturer downloads the student submissions as a zip, the zip contains files with filenames that contain the `q`-number of the student.
The problem is that we have to grade students by name, not by `q`-number, and that we do not have a simple table linking students to `q`-numbers...

Fortunately, the downloaded zip also contains a series of `.txt` files.
These files also mention a `q`-number in their names, and inside the file, there's a line of text containing the name of the student.

For example, say only one student made the assignment.
When the lecturer downloads the submissions, he will receive a zip with two files:

```text
Submission_q1234567_14-1-2017.txt
Submission_q1234567_14-1-2017.js
```

where the `.js` file is the file uploaded by the student.
The `.txt` files contains

```text
Naam: John Johnson (q1234567)
```

Write a script that, given the filename of the zip file, collects all submissions and puts them in directories named after the student.
In the example above, your script should create a directory `submissions/johnson-john` with `Submission_q1234567_14-1-2017.js` in it.

Start with running `prepare.py`, it will generate a zip which your script will have to process.
Don't assume that submissions are all `.js` files.
You can assume though that a submission file never has a name ending on `.txt`.
