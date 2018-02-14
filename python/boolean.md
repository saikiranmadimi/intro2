# Booleans

## Logical Operators
### `and`
The `and` operator evaluates from left to right. It returns the first falsy value it encounters. If there aren't any falsy values, it'll return the last truthy value in the sequence.
### `or`
The `or` operator evaluates from left to right. It returns the first truthy value it encounters. If there aren't any truthy values, it'll return the last falsy value in the sequence.
### `not`
Nothing crazy here. Flips the boolean value from true to false and from false to true.

## Comparison Operators
### `>=`
### `<=`
### `>`
### `<`

## Exercises
1. Write a square function, it should return the parameter squared.
```python
square(10) #returns 100
square(5) #returns 25
square(-2) #returns 4
```
2. Write a negate function.
```python
negate(5) #returns -5
negate(-15) #returns 15
negate(0) #returns 0
```
3. Given the parameters x, y, and z: return the result of the expression equivalent to "three times x plus half of y, all divided by twice z".
```python
funkyCalc(1, 1, 1) #returns 1.75
funkyCalc(3, 2, 1.25) #returns 4.0
funkyCalc(-1, 6, 1) #returns 0.0
```
4. Calculate and return the Euclidean distance between coordinates given as parameters. To calculate a square root, raise to the 1/2 power.
```python
distance(3, 0, 0, 4) #returns 5.0
distance(1, 0, 2, 0) #returns 1.0
distance(0, 0, 8, 15) #returns 17.0
```
5. Write a function to convert Fahrenheit temperatures into Celsius.
```python
ftoc(32) #returns 0.0
ftoc(212) #returns 100.0
ftoc(-40) #returns -40.0
```
6. Write a function to convert Celsius temperatures into Fahrenheit.
```python
ctof(0.0) #returns 32.0
ctof(100.0) #returns 212.0
ctof(-40) #returns -40.0
```
7. Write a function that evaluates a quadratic equation in the form y = ax^2 + bx + c. It accepts the parameters in the order a, b, c, x and returns the y value.
```python
evalQuadratic(1, 0, 3, 1) → 4
evalQuadratic(1, 2, 3, 1) → 6
evalQuadratic(1, 0, 3, 2) → 7
```
