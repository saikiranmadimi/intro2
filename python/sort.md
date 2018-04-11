# Sorting
As a computer science major in college, you'll find a whole class dedicated to data structures and algorithms. Sorting algorithms specifically deal with organizing items by value. BigO Notation is how we express the efficiency of algorithms  -
[Big O CheatSheet](http://bigocheatsheet.com/). We won't be covering the efficiency of algorithms in this class, but that's something you'll come across in AP!

# Devise your own sorting algorithm - some tools
## `.append()`
the append method adds the argument given to the end of the list
```python
nums = []
nums.append(1)
nums.append(2)
nums.append(3)
```

## `.pop()`
the pop method removes an element at a particular index
```python
nums = [1, 2, 3, 4, 5]
nums.pop(0) # returns 1 and turns nums into [2, 3, 4, 5]
```

## `.remove()`
the remove method removes the first occurrence of the argument passed
```python
nums = [1, 2, 3, 4, 5, 1]
nums.remove(1) # nums is now [2, 3, 4, 5, 1]
```

## adding lists or concatenation
```python
[1, 2, 3] + [4, 5] # returns [1, 2, 3, 4, 5]
```

# Quick Sort
1. Pick an element, called a pivot, from the array.
2. Partitioning: reorder the array so that all elements with values less than the pivot come before the pivot, while all elements with values greater than the pivot come after it (equal values can go either way). After this partitioning, the pivot is in its final position. 
3. Recursively apply the above steps to the sub-array of elements with smaller values and separately to the sub-array of elements with greater values.
[Visualization](http://sorting.at/)
