# Loops

## Syntax
Below you'll find the syntax for `while`
```python
while <test>:
  # loop body code
  # loop body code
  # ...
```

Below you'll find the syntax for `raw_input`
```python
num = raw_input("Input the number 5: ")

if num != "5":
    print "you didn't give me a high five :("
```

## Examples
1. Asking for a number and checking to make sure it's a valid integer
2. Printing out all the numbers within a certain range
3. Printing out the characters of a string

## Exercises
1. Writing a python script and keeps asking for an integer until it receives a valid input.
2. Print out all the even numbers between 100 and 800 inclusive.
3. Write a function that receives a number and returns true or false whether a number is a prime number. You should only be inputting numbers greater than 1
```python
isPrime(0) #returns the message "invalid input. please enter a number greater than 1: "
isPrime(1) #returns the message "invalid input. please enter a number greater than 1: "
isPrime(2) #returns True
isPrime(5) #returns True
isPrime(8) #returns False
```
4. Write a function that receives a string and returns the string with alternating cases.
```python
wackyCase("hello") #returns "hElLo"
wackyCase("pikachu") #returns "pIkAcHu"
```
