# Explanations

Download [your group schedule](rooster.ucll.be) for an entire year as an iCal file.
Write a script that reads the file and computes how many hours is scheduled for each day.
Also count gaps: if there is one course scheduled at 8-9 and one at 16-17 on one day,
this counts as 9 hours, not as 2.

Let the script print a table with the following information:

* Date
* Start of day (start of earliest course)
* End of day (end of latest course)
* Total duration (including gaps)

Sort this table according to total duration, in descending order.
Run the solution to get an example.

```bash
$ python solution.py schedule.ics
```

You might want to rely on the `ics` python module. It is not installed by default,
so you will need to [find a way](https://pypi.org/project/ics/) to install it.
