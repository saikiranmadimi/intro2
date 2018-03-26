## Python Exam 1

#### Question 1 - Evaluate the expression below.
```python
4 % 3 / 8 + 7 * 2 - 9
```
**a.** 5 
**b.** 4 
**c.** 2 
**d.** 0 
**e.** None of the above
#### Question 2 - Which one of the following isn't matched up with the correct output?
```python
def wut(arg):
  if arg:
    return "truthy"
  else:
    return "falsy"
```
**a.** `wut(0)` //returns "falsy" <br>
**b.** `wut("hello")` //returns "truthy" <br>
**c.** `wut(-4)` //returns "falsy" <br>
**d.** `wut("")` //returns "falsy" <br>
**e.** `wut(True)` //returns "truthy"

#### Question 3 - Which of the following conversions would work?
**a.** `int(7.3)` <br>
**b.** `float("hello")` <br>
**c.** `str(123)` <br>
**d.** a & c <br>
**e.** a & b
#### Question 4 - What gets printed from running the code below?
```python
def doWork():
  x = 0
  while x < 100:
    if x == "17":
      return "done early"
  return "finished"

print doWork()
```
**a.** `"done early"` <br>
**b.** `"finished"` <br>
**c.** `None` <br>
**d.** None of the above

#### Question 5 - What does python use to group commands inside of a function, loop, or if/else block?
**a.** () <br>
**b.** [] <br>
**c.** new lines <br>
**d.** {} <br>
**e.** none of the above

#### Question 6 - What gets printed from running the code below?
```python
def someFunction(word):
  idx = 0
  output = ""
  while idx < len(word):
    if idx % 3 == 0:
      output = output + word[idx].upper()
    else:
      output = output + word[idx].lower()
    idx = idx + 1
  return output

print someFunction("hello world")
```
**a.** `"HelLo WorLd"` <br>
**b.** `"Hello World"` <br>
**c.** `"HeLlO WoRlD"` <br>
**d.** `"hElLo wOrLd"` <br>
**e.** None of the above

#### Question 7 - Given the function definition below, what is stored in `egg` when you run the command: `egg = chicken(chicken(chicken(8)))`?
```python
def chicken(food):
  if food % 2 == 0:
    return food + 1
  elif food > 5:
    return food  / 3
  else:
    return food / 2
```
**a.** 0 <br>
**b.** 1 <br>
**c.** 2 <br>
**d.** 3 <br>
**e.** None of the above

#### Question 8 - Given the function definition below, what is stored in `powerOfTwo` when you run the command: `powerOfTwo = raiseTwo()`?
```python
def raiseTwo():
  x = 3
  output = 2
  while x < 20:
    output = output * 2
    x = x + 2
  return output
```
**a.** 256 <br>
**b.** 512 <br>
**c.** 1024 <br>
**d.** 2048 <br>
**e.** None of the above
#### Question 9 - How many times will the code below print `poke`?
```python
annoy = 26
while annoy > 12:
  print "poke"
  annoy = annoy - 3
```
**a.** 4 <br>
**b.** 5 <br>
**c.** 6 <br>
**d.** 7 <br>
**e.** None of the above
#### Question 10 - What gets printed when the code below is run?
```python
def mysteryFunction(num):
  output = 0
  while num > 0:
    output = output + num % 10 * 2
    num = num / 10
  return output

print mysteryFunction(2143)
```
**a.** 7 <br>
**b.** 10 <br>
**c.** 18 <br>
**d.** 20 <br>
**e.** None of the above
#### Question 11 - What does the function `highFive()` return?
```python
def highFive():
  x = 5
  if x >= 5:
    x = x + 5
  if x >= 10:
    x = x + 5
  if x >= 15:
    x = x + 5
  return x
```
**a.** 5 <br>
**b.** 10 <br>
**c.** 15 <br>
**d.** 20 <br>
**e.** None of the above
#### Question 12  - What gets printed by running the code below?
```python
def isPythagoreanTriple(a, b, c):
  a ** 2 + b ** 2 == c ** 2

print isPythagoreanTriple(3, 4, 5)
```
**a.** True <br>
**b.** False <br>
**c.** 0 <br>
**d.** None

#### Question 13a
Write a function `mySymbol` that receives one character in the form of a string. It should return `True` if the character is one of the following 10 symbols: `!`, `@`, `#`, `$`, `%`, `^`, `&`, `*`, `(`, `)` and `False` if the character is not a character within this group of 10. You must use a `while` loop.
```python
mySymbol("8") #returns False
mySymbol("h") #returns False
mySymbol("!") #returns True
```
#### Question 13b
Write a function `myDigit` that receives one character in the form of a string. It should return `True` if the character is a numerical digit and `False` if the character is not. You must use a `while` loop.
```python
myDigit("8") #returns True
myDigit("h") #returns False
myDigit("!") #returns False
```

#### Question 14a
Write a function `madeOfSymbols` that receives a string. It'll return `True` if the string has at least 3 of the following symbol characters: `!`, `@`, `#`, `$`, `%`, `^`, `&`, `*`, `(`, `)`. It'll return `False` otherwise. You must use a `while` loop and the `mySymbol` function you wrote in the previous problem.
```python
madeOfSymbols("h3ll0") #returns False
madeOfSymbols("*@%^!$") #returns True
madeOfSymbols(")(#3209") #returns True
madeOfSymbols("hola!!") #returns False
```
#### Question 14b
Write a function `madeOfDigits` that receives a string. It'll return `True` if the string is made of all numbers. It'll return `False` otherwise. You must use a `while` loop and the `myDigit` function you wrote in the previous problem.
```python
madeOfDigits("h3ll0") #returns False
madeOfDigits("*@%^!$") #returns False
madeOfDigits(")(#3209") #returns False
madeOfDigits("35918") #returns True
```
