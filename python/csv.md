## File Operations
assume fn is a filename (a string)
assume fh is a file handle

```python
open(fn, 'w') #returns a file object to write to (overwrites)
open(fn, 'r') #returns a file object to read from
open(fn, 'a') #returns a file object to append onto
fh.read() #returns a string containing the entire contents of the file
fh.readline() #returns the next line in the file (a string)
fh.readlines() #returns a list, each item is a line
fh.write(s) #inserts string s to a file and returns None
fh.close() #closes the file object; returns None
```

1. Implement a text file copy program that reads in a file name to
   copy then creates a new file that is a copy however all the characters
   in the copy are in upper case. The created file's name should have
   the format   <originalCOPY.prefix>.

   For example,
      Original Name                Copy
      =============================================
      stuff.txt                    stuffCOPY.txt
      ex01.py                      ex01COPY.py


## CSV Files
CSV stands for comma separated values. Programs like Microsoft Excel and Google Sheets can read comma separated value files.


## Sample Text 
Use the text below for your .txt file.
```
PREFACE

Most of the adventures recorded in this book really occurred; one or two
were experiences of my own, the rest those of boys who were schoolmates
of mine. Huck Finn is drawn from life; Tom Sawyer also, but not from an
individual--he is a combination of the characteristics of three boys whom
I knew, and therefore belongs to the composite order of architecture.

The odd superstitions touched upon were all prevalent among children and
slaves in the West at the period of this story--that is to say, thirty or
forty years ago.

Although my book is intended mainly for the entertainment of boys and
girls, I hope it will not be shunned by men and women on that account,
for part of my plan has been to try to pleasantly remind adults of what
they once were themselves, and of how they felt and thought and talked,
and what queer enterprises they sometimes engaged in.

THE AUTHOR.

HARTFORD, 1876.
```
