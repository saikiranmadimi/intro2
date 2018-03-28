# Recursion

## Default parameters/arguments
```python
def hello(name = "john"):
  return "hello " + name

print hello()
print hello("world")
```

## Euclid's algorithm
Euclid's algorithm is a way to identify the greatest common factor of two numbers without working out the prime factorization.
![gcf](https://i.ytimg.com/vi/IuyU9Ng75Xc/maxresdefault.jpg)
```python
gcf(81, 36) # returns 9
gcf(24, 8) # returns 8
```

## Subset construction
A set A is a subset of a set B if A is "contained" inside B, that is, all elements of A are also elements of B. 
```python
subset([True]) # returns [[], [True]]
subset(["a", "b"]) # returns [[], ["a"], ["b"], ["a", "b"]]
subset([1, 2, 3]) # returns [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
```
