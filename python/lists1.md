# Lists (Arrays)
Lists or Arrays allow you to store multiple values within one data structure. Lists and arrays can be used interchangeably. You can put an element of any datatype found in python into an array.

## How to make a list
```python
pokemon = ["bulbasaur", "charmander", "squirtle"]
```

## How to access an element within a list
```python
colors = ['red', 'blue', 'green']
colors[0]    ## red
colors[2]    ## green
```

## How to find the length of a list
```python
colors = ['red', 'blue', 'green']
len(colors)  ## 3
```

## How to loop through a list
You can loop through a list the same way you loop through a string.
```python
colors = ["red", "blue", "yellow", "green"]
idx = 0
while idx < len(colors):
  print colors[idx]
  idx = idx + 1
```

## Assigning values
Unlike strings, you can change the values of elements
```python
a = [1, 2, 3]
a[1] = 4
a #returns [1, 4, 3]
```

## Pass by reference
```python
a = [1, 2, 3]
b = a
a[1] = 4
a # returns [1, 4, 3]
b #What does `b` look like now????
```

## Exercises
Complete the list problems (no loops) and list problems (single loop) on this [CodingBat](http://codingbat.com/home/konstans@stuy.edu/intro) page.
