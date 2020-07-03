# Assignment

The file `input.txt` contains a git log, i.e. a series of commits.
Each commit has an author.

```text
commit f626da3137ac22d4b962806e989266a85001e55d
Author: Nathan Van Beneden <nathan.vanbeneden@student.ucll.be>
Date:   2010-01-01 03:37:14

    Closed #5182

commit b9c87ee687ad423cd0c1a68d7eea5e210cbb78d0
Author: Liwady Yermolovich <liwady.yermolovich@student.ucll.be>
Date:   2010-01-01 03:58:58

    Closed #8963

commit c27eda6c4a2b817ff7a7daf2da6909f5293ca307
Author: Connor Van Esbroeck <connor.vanesbroeck@student.ucll.be>
Date:   2010-01-01 06:59:21

    Closed #6278

commit 341686ec9142e34926e19f97576e583a210c3640
Author: Liwady Yermolovich <liwady.yermolovich@student.ucll.be>
Date:   2010-01-04 19:19:02

    Closed #7545

commit 406742df874c978d729f7b8026adacb9d44168a9
Author: Connor Van Esbroeck <connor.vanesbroeck@student.ucll.be>
Date:   2014-03-16 01:23:26

    Closed #372

commit 52f92ffcd140472eec116ab75367308def52155b
Author: Connor Van Esbroeck <connor.vanesbroeck@student.ucll.be>
Date:   2014-03-17 18:05:34

    Closed #3399
```

Count the number of commits done by author and write the results
to `output.txt`:

```text
Connor Van Esbroeck: 3
Liwady Yermolovich: 2
Nathan Van Beneden: 1
```

Order the entries by descending number of commits.
You can assume that each author has a different number of commits.
