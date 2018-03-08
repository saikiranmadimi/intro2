# While Loops

## How to print the characters of a string backwards
### Option 1
```python
def printBack(word):
  idx = len(word) - 1
  while idx > 0:
    print word[idx]
    idx = idx - 1
```
### Option 2
```python
def printBack(word):
  idx = -1
  while idx >= -(len(word)):
    print word[idx]
    idx = idx - 1
```


1. Ask the user for a number between 1 and 10 inclusive, if the user doesn't comply then keep asking. <br>
Test Run:
```
Enter a number between 1 and 10 inclusive: 11
Enter a number between 1 and 10 inclusive: -3
Enter a number between 1 and 10 inclusive:  2
Thanks
```
2. Ask the user for a positive integer, then print all the odd numbers from 1 to n. <br>
Test Run:
```
Enter a positive #: 10
1
3
5
7
9
DONE
```
3. Ask the user for two positive integers, and print all the odd integers from a to b. <br>
Test Run #1:
```   
Enter a positive integer: 2
Enter another: 15
3
5
7
9
11
13
```
Test Run #2:
```   
Enter a positive integer: 9
Enter another: 1
1
3
5
7
```

4. Read in a positive integer, n and then print all the positive divisors of n. <br>
Test Run #1:
```
Enter a positive integer: 1
1
```
Test Run #2:
```
Enter a positive integer: 5
1
5
```
Test Run #3:
```
Enter a positive integer: 24
1
2
3
4
6
8
12
24
```

5. Write a function that receives a number and returns true or false whether a number is a prime number. You should only be inputting numbers greater than 1
```python
isPrime(0) #returns the message "invalid input. please enter a number greater than 1: "
isPrime(1) #returns the message "invalid input. please enter a number greater than 1: "
isPrime(2) #returns True
isPrime(5) #returns True
isPrime(8) #returns False
```
6. Write a function that receives a string and returns the string with alternating cases.
```python
wackyCase("") #returns ""
wackyCase("!3 blah") #returns "!3 BlAh"
wackyCase("hello") #returns "hElLo"
wackyCase("pikachu") #returns "pIkAcHu"
```
