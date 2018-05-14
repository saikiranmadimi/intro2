## Dictionaries

### Syntax
Dictionaries consist of key-value pairs. Each key-value pair is separated by commas. Within each pair, the key precedes the value with a colon in between.
```python
dict = {key1: val1, key2: val2}
```
### Making a dictionary
You can either make a dictionary by calling the `dict()` function or directly hard coding it with curly braces.
```python
D = dict()
D = {1: 4}
```
### Accessing a value
Use square brackets to access the contents of a dictionary in the same way that you use an array or list. The value within the square brackets has to be an existing key within the dictionary.
```python
D = {"hello": "world", 2: 3, True: False}
D["hello"] #returns "world"
D[2] #returns 3
D[True] #returns False
```
### Creating a new key-value pair
The way you create a new key-value pair is almost the same way as you access a value. The only difference is you need to follow up accessing a key with an `=` and the value you want to assign.
```python
D = {}
D[4] = 5
D[None] = "Nada"
D #returns {4: 5, None: "Nada"}
```
### Updating a value
The same as creating a new pair. If the key already exists, the value will be updated.
```python
D = {}
D[4] = 5
D[4] = "Four"
D #returns {4: "Four"}
```
### Dictionary Methods
Two important dictionary methods are `.keys()` and `.values()`. Both produce a list of items.
```python
D = {"hello": "world", 2: 3, True: False}
D.keys() #returns ["hello", 2, True]
D.values() #returns ["world", 3, False]
```

### Looping through a Dictionary
Use a loop to iterate through the keys of the dictionary.
```python
D = {"hello": "world", 2: 3, True: False}
for key in D.keys():
  print D[key]
```

## Modules
You can import other files and programs into your python file by placing an `import` statement at the top.
```python
import MODULE
import MODULE_NAME as VARIABLE_NAME
```
You can use the module later in your code.
```python
import math
import random
math.floor(3.14) #returns 3.0
random.random() #returns a float between 0.0 and 1.0
random.randint(a, b)
```

## Activities
1. Write a function that receives a string a returns a dictionary that stores all the characters as keys and the number of their occurrences as values.
```python
countChar("hello world") #returns {"h": 1, "e": 1, "l": 3...}
```
2. Write a function that can process a `.txt` file and returns a dictionary that stores all the words as keys and the number of their occurrences as values. Open a file and use `.read()`.
#####`olivertwist.txt`
```
The evening arrived; the boys took their places. The master, in his cook's uniform, stationed himself at the copper; his pauper assistants ranged themselves behind him; the gruel was served out; and a long grace was said over the short commons. The gruel disappeared; the boys whispered each other, and winked at Oliver; while his next neighbours nudged him. Child as he was, he was desperate with hunger, and reckless with misery. He rose from the table; and advancing to the master, basin and spoon in hand, said: somewhat alarmed at his own temerity:

'Please, sir, I want some more.'

The master was a fat, healthy man; but he turned very pale. He gazed in stupified astonishment on the small rebel for some seconds, and then clung for support to the copper. The assistants were paralysed with wonder; the boys with fear.

'What!' said the master at length, in a faint voice.

'Please, sir,' replied Oliver, 'I want some more.'
```
3. Write a function to return a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
```python
squareDict() #returns {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
```
4. Write a function to return a dictionary where the 10 keys are random numbers between 1 and 100 and the values are square of keys. Use the `random` module and `randint()` method.
```python
randomSquareDict() #returns {25: 625, 2: 4, 9: 81, 4: 16, 11: 121...}
```

**Go to Room 803 Tomorrow for Robots** Bring a flashdrive!
![Programming Robots](https://imgs.xkcd.com/comics/self_driving_2x.png)
