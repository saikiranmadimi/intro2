# Python Exam 2 Practice Questions

## Pair Programming
Communication is key in pair programming.
* Driver
  - only one that does any typing, only one that touches the keyboard
  - should not write any code on their own without discussing with the navigator
  - implements the solution decided on by the pair
* Navigator
  - provides the direction the code is taking
  - has to be verbal and vocal in articulating their train of thought

**What do you think some benefits of pair programming are? What do you think so pitfalls are?**

## Question 1
Write a function `isDNA` that receives a string and checks to see if the string consists of the letters: `A`, `T`, `C`, `G`. Assume all characters are capitalized - you don't need to consider lowercase letters.
```python
isDNA("GATTACA") # returns True
isDNA("ATTACG") # returns True
isDNA("AT2531") # returns False
```

## Question 2
Write a function, `transcribe` that receives a string that represents a strand of DNA. Its output should be the corresponding strand of RNA. The DNA string should only consist of the letters: `A`, `T`, `C`, `G`. `transcribe` will produce a string of RNA mapping `A` => `U`, `C` => `G`, `G` => `C`, `T` => `A`. If the function does not receive a valid strand of DNA, it'll print out `"MUTATION!"`. You can use the function wrote in the previous problem.  
```python
isDNA("GATTACA") # returns "CUAAUGU"
isDNA("ATTACG") # returns "UAAUGC"
isDNA("ATC9!09") # returns "MUTATION!"
```

## Question 3
```python
num = int(raw_input('enter an integer'))
i = 0
while num != 0:
    i = (10 * i) + (num % 10)
    num /= 10
```
a) if n = 123456, what is the value of num and i after executing this code?
b) if n = 400, what is the value of num and i after executing this code?

## Question 4
Write a function that receives a string and outputs whether the string is a valid IPv4 address. Anything between 0.0.0.0 and 255.255.255.255 would return true.
```python
isIPValid("195.2.43.5") # returns True
isIPValid("0.4.521.3") # returns False
```

## Question 5
Write a function that performs the Caesar Cipher. The function caesarCipher should receive two arguments: a string and a number. The number specifies how many letters to shift the string by.
```python
caesarCipher("hello", 1) # returns "ifmmp"
caesarCipher("dog", 3) # returns "grj"
```

## Question 6
Given a string and the position of an open parentheses bracket, return the position of the matching closing parentheses bracket.
```python
findClose("He(ll(o) Wor)ld", 2) # returns 12
findClose("(()())", 1) # returns 2
```

## Question 7
Write a function that reads an array and outputs an array of arrays describing the number of each element in the array.
```python
elementCount([2, 1]) # returns [[1, 2], [1, 1]]
elementCount([1, 2, 1, 1]) # returns [[1, 1], [1, 2], [2, 1]]
elementCount(['a', 'a', 'c', 'd', 'e']) # returns [[2, 'a'], [1, 'c'], [1, 'd'], [1, 'e']]
```

## Question 8
Write a function digitalRoot that receives a number and sums each digit until the sum is less than 10.
```python
digitalRoot(121) // returns 4
digitalRoot(746) // returns 8
digitalRoot(6598) // returns 1
```
