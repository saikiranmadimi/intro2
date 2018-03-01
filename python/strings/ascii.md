# ASCII

## Introduction
We learned earlier in the school year that everything within a computer is stored in binary bits and bytes.

## Functions
```python
ord("char")
chr(int)
```
## Escape Sequences
Special characters contained in a string
  - \t tab
  - \n newline
  - \\ backslash
  - \' single quote
  - \" double quote

## Experiment
* Map out the ASCII values of characters in python. What are some strategies to explore the values?
* What are some problems we could run into with ASCII?
* What are some limitations?

## Faces Lab    
```python
hair = "\t" + "|" * 20
eyes = "\t|" + " " * 18 + "|\n"
eyes = eyes * 2
eyes = eyes + "\t|" + " " * 5 + "o" + " " * 6 + "o" + " " * 5 + "|"
ears =  " " * 7 + "_|" + " " * 18 + "|_\n"
ears = ears + ' ' * 6 + "|_" + ' ' * 20 + '_|'
mouth = "\t" + "|" + ' ' * 3 + '|__________|' + ' ' * 3 + "|\n"
mouth = mouth + '\t|' + ' '* 18 + '|'


# output
print hair
print eyes
print ears
print mouth
```

a. Make a `face.py` file and paste the code above into the file. The script should produce a face comprised of ASCII characters. Note the use of escape sequences. You may want to check out the ascii art located at http://chris.com/ascii/

b. Edit the `face.py` to reproduce the faces shown below. (Taken from Owen Astrachan, Computer Science Tapestry).
```
    face 1
	||||||||||||||||
	|   o      o   |
       _|              |_
      |_                _|
	|              |
	|   |______|   |
	|_____    _____|
	     |    |

    face 2
	||||||||||||||||
	|              |
	|  __      __  |
	| !  ! __ !  ! |
	| !o !/  \!o ! |
	| !__!    !__! |
	|              |
	|    ///|\\\   |
	 \            /
	  \     o    /
	   \________/
```
