# Assignment

During the semester, students can earn cake points (how is a well guarded secret.)
At some random times during the semester, cake gets baked and brought to class.
Students can then cash in their well deserved cake points, i.e., exchange one point
for a piece of cake.

To keep track of who has how many cake points, a bit of bookkeeping is required.
This is done through the use of a simple text file containing the following information:

```text
Peter Peterson:3/5
John Johnson:0/2
```

Here, Peter has earned 5 cake points and has already exchanged 3, whereas
John has earned 2 but has not yet cashed in any of them.

However, during chaos that class can be, it is hard to correctly keep track
of who earned and/or cashed in cake points. For this reason, we
simplify the bookkeeping to added simple `+` and `-` symbols:

* A `+` indicates an extra earned cake point.
* A `-` indicates a spent cake point.

Say Peter earns a new cake point, the list becomes

```text
Peter Peterson:3/5 +
John Johnson:0/2
```

If he now chooses to spend it, a `-` is added:

```text
Peter Peterson:3/5 +-
John Johnson:0/2
```

After a while, things might end up as

```text
Peter Peterson:3/5 +-++-+--
John Johnson:0/2 -++-+-++
```

It has now become rather difficult to tell whether someone
still has a positive cake point balance. We need a way
to turn those `+` and `-` back into numbers.
Peter has 4 `+`'s and 4 `-`'s, which means
that he has a total of `5 + 4 = 9` earned
and `3 + 4` cashed in. We can update John in a similar way:

```text
Peter Peterson:7/9
John Johnson:3/7
```

Your task is to write a script that transforms

```text
Peter Peterson:3/5 +-++-+--
John Johnson:0/2 -++-+-++
```

into

```text
Peter Peterson:7/9
John Johnson:3/7
```

* Read your data from `input.txt`.
* Write your data to `output.txt`.
* The order in which the students appear has to be preserved.
