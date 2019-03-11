# Assignment

XKCD, in case you didn't know, is a [webcomic by Randall Munroe](https://en.wikipedia.org/wiki/Xkcd).
Each comic has its own number. At the time of writing, the latest has number 2121.

Write a script that, given a number, fetches information about an XKCD comic and
opens an image viewer showing the comic. If no number is given, the latest comic must be shown.

```bash
$ python xkcd.py 353
month: 12
num: 353
link:
year: 2007
news:
safe_title: Python
transcript: [[ Guy 1 is talking to Guy 2, who is floating in the sky ]]
Guy 1: You're flying! How?
Guy 2: Python!
Guy 2: I learned it last night! Everything is so simple!
Guy 2: Hello world is just 'print "Hello, World!" '
Guy 1: I dunno... Dynamic typing? Whitespace?
Guy 2: Come join us! Programming is fun again! It's a whole new world up here!
Guy 1: But how are you flying?
Guy 2: I just typed 'import antigravity'
Guy 1: That's it?
Guy 2: ...I also sampled everything in the medicine cabinet for comparison.
Guy 2: But i think this is the python.
{{ I wrote 20 short programs in Python yesterday.  It was wonderful.  Perl, I'm leaving you. }}
alt: I wrote 20 short programs in Python yesterday.  It was wonderful.  Perl, I'm leaving you.
img: https://imgs.xkcd.com/comics/python.png
title: Python
day: 5
```

## Approach

Start [here](https://xkcd.com/json.html).

1. Find a way to download this data.
2. Find a way to parse JSON. Don't do this manually, but rely on a Python module instead.
3. Find a way to view an image. Hint: Pillow may help, but this is not the only option. You will probably have to install an extra module. Look for `pip install`.