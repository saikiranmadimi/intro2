# For Loops
for loops allow you to loop through an array or string very easily
```python
arr = [1, 2, 3, 4]
str = "hello world"

for char in str:
  print char

for el in arr:
  print i
```
**problem** how do you access the index within a for loop 😱

## Nested Loops
```python
x = 0
while x < 100:
  y = 0
  while y < 100:
    print x, y
    y += 1
  x += 1
```

## Exercises
1) Given an array of integers, return all pairs that sum up to a specified value k. Use a nested loop.
```python
pairSum([1, 2, 3, 4, 5], 6) # returns [[1, 5], [2, 4]]
pairSum([3, 4, 1, 2, 3, 4, 5, 2, 7], 8) # returns [[3, 5], [4, 4], [1, 7], [3, 5]]
```
2) Write a function that reads an array and outputs an array of arrays describing the number of each element in the array. Use a `for` loop.
```python
elementCount([2, 1]) #returns [[1, 2], [1, 1]]
elementCount([1, 2, 1, 1]) #returns [[1, 1], [1, 2], [2, 1]]
elementCount(['a', 'a', 'c', 'd', 'e']) #returns [[2, 'a'], [1, 'c'], [1, 'd'], [1, 'e']]
```
3) There are 100 open lockers. You close every 2nd locker (so the 2nd, 4th, 6th, ... 100th are all closed). Then, you go to every third locker and open it if it is closed and close it if it is open. You proceed to toggle every nth locker on pass number n. So, for example, on pass number 16 – you will toggle every 16th locker. After your hundredth pass of the hallway, in which you toggle only locker number 100, what lockers are open? You'll want to use a nested loop for this problem. **challenging**
