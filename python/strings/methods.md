# String Methods

## String functions
1. len(string)
  - returns the length of the string
2. string[index]
  - index operator => returns the (index + 1) item, the index position is offset by 1
3. string[from : to]
  - slicing => returns a substring of the string starting at the index from up to but not including the index to
4. string1 + string2
  - concatenation => <a...c> + <d...f> = <a...f>
5. string * N
  - returns an empty string is N <= 0, otherwise returns a copy of the string repeated N times.

## General String methods
You can call string-specific functions by tacking them onto the end of strings either on a string variable or a string itself.
```python
"string".method()
a = "string"
a.method()
```

## Slice
I **NEVER** memorize the slice method. Instead, if I ever need to use it, I come up with a bunch of test cases and test them out in the python shell and discern its behavior.
```python
"hello world"[1:4]
"hello world"[:3]
"hello world"[3:]
```

## Activity
Finish the exercises in `string1.py` and complete `string2.py`.
Go [here](string2.py) for the second exercise.

## Resources
1. [Python CheatSheets](https://ehmatthes.github.io/pcc/cheatsheets/README.html)
