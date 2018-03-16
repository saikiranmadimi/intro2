# 2D Arrays
**lists and arrays are synonymous**

## Making a Matrix
Just place arrays inside of an array.
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

## Looping through a 2D Array
You will need two `while` loops to iterate through a matrix.
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x = 0
while x < len(matrix):
  y = 0
  while y < len(matrix[x]):
    print matrix[x][y]
    y += 1
  x += 1
```

## Exercises
Build a function that returns the winner of a tic-tac-toe game. The function will receive an 3x3 matrix of `X`s and `O`s, return the `X` if there are three `X`s in a row, column, or diagonal, a`Y` if there are three `Y`s in a row, column, or diagonal, and `Tie` if there is no winner. Assume there is at most one winner.
```python
isWinner([["X", "O", "O"],["X", "O", "X"],["O", "X", "X"]]) # returns "O"
isWinner([["O", "X", "X"],["X", "O", "O"],["X", "O", "X"]]) # returns "Tie"
isWinner([["X", "O", "O"],["X", "O", None],["X", None, "X"]]) # returns "X"
```
