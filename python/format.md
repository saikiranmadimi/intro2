# String Formatting

## Basic Formatting
Change the number of `{}` in the string. Change the number of arguments provided to the `.format()` method.
```python
"hello! my name is {}.".format("charles") #returns "hello! my name is charles."
"{} hours".format(10000) #returns "10000 hours"
```
1. How does adding more `{}` affect the behavior of `.format()`
2. How does adding more arguments affect the behavior of `.format()`

## Adding Position to Placeholders
```python
"{0} > {1}".format("Duke", "UNC")
"{1} < {0}".format("Duke", "UNC")
```
1. How does switching the numbers inside of the placeholders change the result?

## Name Placeholders
```python
"{city} is in {country}".format(city="Hong Kong", country="China")
'{pronoun} {verb} {noun}!'.format(pronoun="We", verb='love!' noun="chocolate")
```

## Instructions
You'll need to revisit processing input from the user and opening files to complete this activity.
1. Create a folder `madlibs`.

2. Create two file ins: `jungle.txt` and `newspaper.txt`, save the text below in the appropriate files within the `madlibs` folder.  

3. View the contents of the file jungle.txt.

4. Write the python script, madlibs.py, which reads from **text file** from `jungle.txt`, prompts the user for appropriate input, then generates the file `new_jungle.txt` containing the user's input substituted appropriately into `jungle.txt`.

5. Write a second script to process `newspaper.txt`. You are allowed to modify the values inside the `{}` in `newspaper.txt` for your convenience.

## jungle.txt
```
Once upon a time, deep in an ancient jungle,
therelived a {animal}. This {animal}
liked to eat {food}, but the jungle had
very little {food} to offer. One day, an
explorer found the {animal} and discovered
it liked {food}. The explorer took the
{animal} back to {city}, where it could
eat as much {food} as it wanted. However,
the {animal} became homesick, so the
explorer brought it back to the jungle,
leaving a large supply of {food}.

The End.
```

## newspaper.txt
```
Mrs. Fifi Vanderbold, the {ADJECTIVE} and {ADJECTIVE} heiress,
has filed for divorce from her husband. Percy Vanderbold, the former
{ADJECTIVE} {NOUN} of Harvard, class of '38, now in the
{NOUN} business. Mrs. Vanderbold claimed that her husband
had {VERB (PAST TENSE)} her bed of {COLOR} flowers and tracked
{ADJECTIVE} mud into the house. He also criticized her cooking.
Mr. Vanderbold, when asked to comment, said, "{EXCLAMATION}!
I didn't do it. The pet {ANIMAL} ruined the flowers. And I
offered to take her out to restuarants more often!"
```
