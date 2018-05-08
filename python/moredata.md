### Split and Join

### Write your own split function
```python
split(string, val)
split("Pokemon! Gotta Catch 'Em All", " ") #returns ['Pokemon!', 'Gotta', 'Catch', "'Em", 'All']
split("hello world", "o") #returns ['hell', ' w', 'rld']
```

### Write your own join function
```python
join(arr, val)
join('Pokemon!', 'Gotta', 'Catch', "'Em", 'All'], " ") #returns "Pokemon! Gotta Catch 'Em All"
joing(['hell', ' w', 'rld'], " ") #returns hello world
```

### Tom_Sawyer_Preface.txt
```txt
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
Write a program that outputs the number of characters, words, and lines in the plaintext files that are supplied by the user. Use the text above in your `.txt` file
```command
$ wc filename -> lines words characters file_name  
$ wc Tom_Sawyer_Preface.txt
```
