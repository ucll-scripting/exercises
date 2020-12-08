# Assignment

Write a script that looks up the lyrics of a song.

```bash
$ python lyrics.py "rolling stones" "sympathy for the devil"
Please allow me to introduce myself
I'm a man of wealth and taste
I've been around for a long, long year
Stole many man's soul and faith

I was 'round when Jesus Christ
Had his moment of doubt and pain
Made damn sure that Pilate
Washed his hands and sealed his fate

Pleased to meet you, hope you guess my name
But what's puzzling you is the nature of my game

Stuck around St. Petersburg
When I saw it was a time for a change
Killed the czar and his ministers
Anastasia screamed in vain

I rode a tank, held a general's rank
When the blitzkrieg raged and the bodies stank
Pleased to meet you, hope you guess my name, oh yeah
Ah, what's puzzling you is the nature of my game, oh yeah

I watched with glee while your kings and queens
Fought for ten decades for the gods they made
I shouted out "Who killed the Kennedys?"
When after all, it was you and me

Let me please introduce myself
I'm a man of wealth and taste
And I laid traps for troubadours
Who get killed before they reach Bombay

Pleased to meet you, hope you guess my name, oh yeah
But what's puzzling you is the nature of my game, oh yeah
Get down, baby

Pleased to meet you, hope you guessed my name, oh yeah
But what's confusing you is just the nature of my game
Mmm, yeah

Just as every cop is a criminal
And all the sinners saints
As heads is tails, just call me Lucifer
'Cause I'm in need of some restraint

So if you meet me, have some courtesy
Have some sympathy and some taste
Use all your well-learned politesse
Or I'll lay your soul to waste
Mmm, yeah

Pleased to meet you, hope you guessed my name, mmm yeah
But what's puzzling you is the nature of my game
Mmm, mean it, get down

Woo hoo
Ah yeah, get on down, oh

Ah yeah
Tell me baby, what's my name?
Tell me honey, can ya guess my name?
Tell me baby, what's my name?
I tell you one time, you're to blame

Alright
Oh yeah
What's my name?
Tell me baby, what's my name?
Tell me sweetie, what's my name?
```

## Approach

You can use the url `https://api.lyrics.ovh/v1/artist/title` to fetch the lyrics, where `artist` and `title` must
be replaced by actual data. Keep in mind that URLs are not allowed to contain spaces: these must
be replaced by `%20`. For example, to get the lyrics for Sympathy for the Devil by The Rolling Stones,
you need to download `https://api.lyrics.ovh/v1/rolling%20stones/sympathy%20for%20the%20devil`.

The result will be returned as a json string. Do not parse this manually.
Instead, look for a Python module that performs this task for you.
