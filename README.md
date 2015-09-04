# csvcol
Reorders columns in CSV files.

One often has a CSV file with the right data in its rows, but with
extra columns or with the columns in the wrong order.  This tool
creates a new CSV file with the columns you want in the order you
want.

# Install/config

## Installing prerequisites

If you are on a Mac or Linux machine you already have python
installed.  (You want Python 2.7.x, not Python 3.x.)

If you are on Windows you'll probably need to download from
http://python.org and install as appropriate.  You need to be able to
successfully say `python` from a command prompt.  (The tutorial
installation instructions at
[https://docs.python.org/2/tutorial/interpreter.html](https://docs.python.org/2/tutorial/interpreter.html)
show you how to add `python` to the `path` environment variable.)

# Example

Suppose that you are expecting a CSV file where each row has a
person's Name, Age, Height, and HighScore, but someone instead gives
you a CSV file with Height, Weight, Name, Age, HighScore,
NumberOfPlays, and ShoeSize.  Worse yet, suppose that every time they
give you this CSV file the order of the columns is scrambled so that
you never know whether they'll give you:

```
Height,Weight,Name,Age,HighScore,NumberOfPlays,ShoeSize
```

or

```
Age,Weight,Height,NumberOfPlays,HighScore,ShoeSize,Name
```

or even

```
NumberOfPlays,Age,Name,Height,ShoeSize,HighScore,Weight,Address,LikesIceCream
```

"Ah," you say, "that should never happen.  Please fix it."  Everyone
agrees that you're right, but you keep receiving very slightly
out-of-spec CSV files.

"But we _always_ generate consistent CSV files," your supplier says,
but they're simply incorrect.  (Maybe they should use this script!)

"The spec doesn't allow that," everyone says, but CSV files with extra
and out-of-order columns are the only files that ever arrive.

But you can still deal with the problem by fixing the CSV file like this:

```bash
./csvcol.py slightlywrong.csv Name,Age,Height,HighScore > right.csv
```

or

```bash
python csvcol.py slightlywrong.csv Name,Age,Height,HighScore > right.csv
```

# FAQ

**Q:** It dumps my csv data to the screen!  Can I have it in a file instead?

**A:** Yes.  You need the
  [redirect operator](http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-3.html),
  which is the little greater than sign in the examples above.  If you
  forget that part then the reformatted CSV data will get dumped to
  your screen instead of into a file.

**Q:** Can't I just do this from Excel?

**A:** Yes, but that requires a person---you---to pay attention to and
  to interact with the computer every time you want to modify a CSV
  file.  Doing a tedious and repetitive thing like this by hand is a
  waste of your life; you should be interacting with your friends and
  family instead, or playing outside.  Computers should do this work
  for you!  Also, your competitors might have already automated away
  all their tedious CSV file manipulation (by using a script like this
  one, maybe), and they'll soon outcompete you in the marketplace
  which could mean that you have plenty of time to pursue the rest of
  your life also.  So either way, you win.

**Q:** What if I want to look at a huge CSV file to see what the columns are?

**A:** You want the `head` command.  On a Mac or Linux machine, try
  running `head enormous.csv` (or even `head -n 1 enormous.csv`) and
  be amazed at how instantaneously you can see what columns are in the
  csv file.  There's probably a Windows equivalent, but I don't know
  what it would be.

# License

MIT --- See LICENSE.
