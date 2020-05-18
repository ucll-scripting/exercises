# Assignment

The file `input.txt` contains a git log. For example:

```data
commit 42d4a2b1f13dcce0236d52572bae5fd423b68a86
Author: Arne Ausloos <arne.ausloos@student.ucll.be>
Date:   2010-01-01 02:26:07

    Closed #1377

commit 3d279d2d6357ee5906969df803225e9ed989b42f
Author: Jens Aerts <jens.aerts@student.ucll.be>
Date:   2010-01-01 05:35:59

    Closed #3023

commit 5d99f02b6f94fd34b7a364eb4186b58de84cdd6e
Author: Connor Coremans <connor.coremans@student.ucll.be>
Date:   2010-01-01 15:48:03

    Closed #6881

commit 2c0b0ace974c8b1f99b8ddac08478f612f7720f4
Author: Arne Ausloos <arne.ausloos@student.ucll.be>
Date:   2010-07-03 18:26:56

    Closed #3912
```

Extract the authors and write them in alphabetical order to `output.txt`.
Each author should only be listed once.

```text
Arne Ausloos
Connor Coremans
Jens Aerts
```
