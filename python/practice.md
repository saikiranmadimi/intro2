# Practice Exam

1. Evaluate
```python
5 + 4 / 3.0
```
- What is the order of operations?
- What is the result of multiplying an integer with a float?

2. Evaluate
```python
100 % 6 + 8 % 12
```
What does `%` do? How does it fit into the order of operations?

3. Evaluate
```python
int(3.14)
```
How does the `int` function change a float?

4. Given the function definition below, what is the value of x when you run the command: `x = womp(womp(4))`
```python
def womp(x):
    if x < 10:
      return 2 + 2 * x
    else:
      return x / 2
```

5. Given the function definition below, what is printed when you call `grade(93)`?
```python
def grade(score):
  if score > 75:
    print "C"
  if score > 85:
    print "B"
  if score > 90:
    print "A"
```
Why?

6. How many times does this loop print `stuy`?
```python
i = 8
while i <= 20:
    print "stuy"
    i = i + 2
```

7. How many times does this loop print `SING!`?
```python
i = 100
while i >= 10:
  print "SING!"
  i = i / 10
```

8. Given the function below:
```python
def fruit(choice):
  if choice % 3 == 0:
    return "apple"
  if choice > 5:
    return "orange"
  if choice <= 0:
    return "BANANA"
```
What gets printed when you run the command: `print fruit(7)`
