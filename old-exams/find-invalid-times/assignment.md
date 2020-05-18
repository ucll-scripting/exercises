# Assignment

Take a peek at `input.txt`: apart from random text, it also
contains times (`hh:mm:ss`). In order to be correct,
a time must adhere to the following constraints:

* The hour must be between `0` and `23`.
* The minutes must be between `0` and `59`.
* The seconds must be between `0` and `59`.

We suspect that many times appearing in `input.txt`
are erroneous. We therefore ask of you to
look for all pieces of text that appear
to be times and check which ones are invalid.
List all invalid times together with the line number
on which they appear and write the results to `output.txt`.

* The first line has index `1`.
* Times are always formatted as `hh:mm:ss`.
* The invalid times should be listed in the same order as in which they appear in `input.txt`.

## Example

Say `input.txt` contains

```text
52444.vj5cm 07:10:05 07:11:25 .5qfahjtaikgr3buwv7wjwixm9.95fr8zs12m8i8oyga5592 03:44:24 gm2qlx5..eid6j9gripuk8m7 09:62:14 26:23:55 wkdo42f.wkbdv6dk257mtsy zzqrzgo9bbwms28guz4un3d7bzgbt82sclmgvb
07:24:32 11:39:55 np24x4qg2gn6aw1kdrr 05:47:57
13:06:55 6ltv8sb916per8m4pxlh8nz9enzjp48uw 22:32:35 17:41:47 ohqejeqtyeulk.dgukrupsbq .au9llkpeszz1sklfd.c5rwratkcwhtr9h8x4 22:09:00
11:70:55 a2il.rrye238srir9ay4xlsvp5qc7uit9yb1p7e8fjn8 02:40:06 20:03:62 17:21:67
```

The first line contains 5 times:

* `07:10:05`: correct
* `07:11:25`: correct
* `03:44:24`: correct
* `09:62:14`: invalid minutes
* `26:23:55`: invalid hours

The second and third lines contain valid times, whereas the fourth line contains 4 times, 3 of which are invalid.

These mistakes are to be written to `output.txt` in the following format:

```text
1 09:62:14
1 26:23:55
4 11:70:55
4 20:03:62
4 17:21:67
```
