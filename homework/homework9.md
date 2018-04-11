# Homework 9

1) Write a function that reads an array and outputs an array of arrays describing the number of each element in the array. Use a `for` loop.
```python
elementCount([2, 1]) #returns [[1, 2], [1, 1]]
elementCount([1, 2, 1, 1]) #returns [[1, 1], [1, 2], [2, 1]]
elementCount(['a', 'a', 'c', 'd', 'e']) #returns [[2, 'a'], [1, 'c'], [1, 'd'], [1, 'e']]
```
2) There are 100 open lockers. You close every 2nd locker (so the 2nd, 4th, 6th, ... 100th are all closed). Then, you go to every third locker and open it if it is closed and close it if it is open. You proceed to toggle every nth locker on pass number n. So, for example, on pass number 16 – you will toggle every 16th locker. After your hundredth pass of the hallway, in which you toggle only locker number 100, what lockers are open? You'll want to use a nested loop for this problem. **challenging**
