# Assignment

In Mario Kart Grand Prix mode, 12 players race against each other on four courses.
With each race, players earn points depending on their ranking: the first to reach the finish line gets 15 points, the second 12 points, etc.
The sum of these points determines the final ranking.

This exercise requires you to write a script to similarly determine the final ranking for a variant on Mario Kart:

* Instead of 4 courses, we have 100.
* Instead of 12 competitors, we have 100.
* The first to cross the finish line earns 100 points, the second 99, the third 98, etc.

`input.txt` contains the rankings of each of the 100 races.

* The first 100 lines correspond to the ranking of the first race.
* The following 100 lines correspond to the ranking of the second race.
* The following 100 lines correspond to the ranking of the third race.
* Etc.

The script should produce a file named `output.txt` that contains the names of the top 10 participants, one name per line.

## Example

For this example, we will pretend there are only 3 races and 5 participants named A, B, C, D and E.
Say we also only need to determine the top 3 of the final ranking.

Say `input.txt` contains the following:

```text
A
B
C
D
E
A
C
B
D
E
B
A
D
E
C
```

The first five lines represent the ranking of the first race:

1. A
2. B
3. C
4. D
5. E

A finished first and therefore gains 5 points.
B is second and earns 4 points.
C gets 3 points, D 2 points and E 1 point.

The second race has ranking

1. A -> +5
2. C -> +4
3. B -> +3
4. D -> +2
5. E -> +1

The final race has ranking

1. C -> +5
2. A -> +4
3. D -> +3
4. E -> +2
5. B -> +1

We take the sum of the points earned by each competitor:

* A: 5 + 5 + 4 = 14
* B: 4 + 3 + 1 = 8
* C: 3 + 4 + 5 = 12
* D: 2 + 2 + 3 = 7
* E: 1 + 1 + 2 = 4

The final ranking becomes

1. A with 14 points
2. C with 12 poitns
3. B with 8 points
4. D with 7 points
5. E with 4 points

We are supposed to produce the top 3 final ranking.
`output.txt` should therefore contain

```text
A
C
B
```
