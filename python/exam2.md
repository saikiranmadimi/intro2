### Python Exam 2
Name / Pd:
###### Question 1 - Which of the following choices return `True`?
```python
def wut(arg):
  if arg:
    return True
  else:
    return False
```
**a.** `wut(0)`
**b.** `wut(3)`
**c.** `wut(-4)`
**d.** choices `b` and `c`
**e.** all of the choices
###### Question 2 - Evaluate the code below.
```python
def mysteryFunction(x):
  y = 0
  while x != 0:
    y += 1
    x -= 3
  return y
print mysteryFunction(8)
```
**a.** 4
**b.** 3
**c.** 0
**d.** `None`
**e.** None of the above
###### Question 3 - Which of the following conversions would work?
**a.** `int(7.3)`
**b.** `int("123")`
**c.** `int(8)`
**d.** choices `a` and `c`
**e.** all of the above

###### Question 4 - What gets printed from running the code below?
```python
def doWork():
  x = 0
  while x < 100:
    if x == 31:
      return "done early"
    x = 2 * x + 1
  print "finished"
print doWork()
```
**a.** `"done early"`
**b.** `"finished"`
**c.** `None`
**d.** None of the above
###### Question 5 - What gets printed from running the code below?
```python
def someFunction(arr):
  idx = 0
  output = []
  while idx < len(arr):
    if idx % 2 == 0:
      output.append(arr[idx])
    idx = idx + 2
  return output
print someFunction([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
```
**a.** `[2, 4, 6, 8, 0]`
**b.** `[1, 3, 5, 7, 9]`
**c.** `[]`
**d.** None of the above
###### Question 6 - Given the function definition below, what is stored in `egg` when you run the command: `egg = chicken(chicken(chicken(8)))`? **
```python
def chicken(food):
  if food % 2 == 0:
    food = food + 1
  if food > 5:
    return food  / 3
  else:
    return food / 2
```
**a.** 0
**b.** 1
**c.** 2
**d.** 3
**e.** None of the above
###### Question 7 - What will get printed from running the code below?
```python
def youngerSibling(age):
  bother = ""
  while age >= 0:
    bother += "poke"
    age -= 1
  return bother
print youngerSibling(5)
```
**a.** `"pokepokepoke"`
**b.** `"pokepokepokepoke"`
**c.** `"pokepokepokepokepoke"`
**d.** `"pokepokepokepokepokepoke"`
**e.** None of the above
###### Question 8 - What gets printed when the code below is run?
```python
def mysteryFunction():
  x = 0
  output = 0
  while x <= 50:
    if x % 2 == 0 and x % 5 == 0:  
      output += x
    x += 1
  return output
print mysteryFunction()
```
**a.** 50
**b.** 100
**c.** 150
**d.** 0
**e.** None of the above
###### Question 9 - What does the function `lowFive()` return?
```python
def lowFive():
  x = 5
  if x >= 5:
    x += 5
  if x >= 10:
    x -= 5
  if x <= 15:
    x *= 5
  return x
```
**a.** 5
**b.** 10
**c.** 20
**d.** 25
**e.** None of the above


###### Question 10  - What is the value of `cube` after running the code below?
```python
cube = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
cube[0][0][0] = 0
cube[1][0][1] = 0
cube[0][1][0] = 0
cube[1][1][1] = 0
```
**a.** `[[[0, 2], [0, 4]], [[5, 0], [7, 0]]]`
**b.** `[[[0, 2], [3, 4]], [[0, 0], [7, 0]]]`
**c.** `[[[1, 0], [3, 4]], [[5, 0], [0, 8]]]`
**d.** None of the above
###### Question 11
Write a function `isOddBinary` that can receive either a string or an integer. Should return `True` if and only if it is both a binary number and odd. Should return `False` otherwise. Hint: you may want to write a helper function that checks to see if the input is binary first. Also think about what an odd number looks like in binary form.
```python
mySymbol("010101010110") #returns False
mySymbol(010101010110) #returns False
mySymbol("010101010111") #returns True
mySymbol(010101010111) #returns True
mySymbol("123") #returns False
mySymbol(123) #returns False
```
###### Question 12
Write a function `isSorted` that receives an array of numbers. `isSorted` should return `True` only if the array is ordered from least to greatest. Otherwise, it'll return `False`. You **cannot** use the built-in `.sort()` method.
```python
isSorted([1, 2, 3, 4, 5, 6]) # returns True
isSorted([1, 2, 4, 3, 5, 6]) # returns False
isSorted([-1, 1, 2, 4, 5, 6]) # returns True
isSorted([1, 2, 0, 4, 5, 6]) # returns False
```
