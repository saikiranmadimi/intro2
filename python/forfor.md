# For Loops
For example
```python
arr = [1, 2, 3, 4, 5, 6]
for num in arr:
  if num % 2 == 0:
    print num
```
While example
```python
arr = [1, 2, 3, 4, 5, 6]
x = 0
while x < len(arr):
  if arr[idx] % 2 == 0:
    print arr[idx]
  x += 1
```
## pairSum solution
```python
def pairSum(arr, tgt):
  x = 0
  output = []
  while x < len(arr):
    y = x + 1
    while y < len(arr):
      if arr[x] + arr[y] == tgt:
        output.append([arr[x], arr[y]])
      y += 1
    x += 1
  return output
```

## Exercises
1) Write a function that receives an array and removes all the duplicate values in that array returning an array with only unique values. Try and find two different solutions - at least one should use a nested loop.
```python
removeDups(["apples", "watermelon", "oranges", "oranges", "oranges"]) # returns ["apples", "watermelon", "oranges"]
removeDups([1, 1, 1, 1, 1, 1]) # returns [1]
removeDups([1, 3, 1, 2, 3, 4, 1, 2, 3, 5, 5]) # returns [1, 3, 2, 4, 5]
```

2) Write a function that receives two arrays and produces the cartesian product of the two arrays. The first item in the pair produced should come from the first array and the second item should come from the second array.  ![Cartesian product](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Cartesian_Product_qtl1.svg/501px-Cartesian_Product_qtl1.svg.png)
```python
cartyP([1, 2],[3, 4]) #returns [[1, 3], [1, 4], [2, 3], [2, 4]]
cartyP([1, 2, 3], [1, 2]) #returns [[1, 1], [1, 2], [2, 1], [2, 2], [3, 1], [3, 2]]
```
