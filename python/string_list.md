# Split & join

## `split`
There exists a `split` method that takes a string and provides a list of strings that are made from taking out the string provided in the argument.
```python
a.split(b) # where a is a string and b is a string
"hello".split("")
"hello".split("e")
"hello".split("l")

```
## `join`
There exists a `join` method that takes a list of strings and joins the strings together.
```python
a.join(b) # where a is a string and b is a list of strings
"".join(["a", "b", "c"])
" ".join(["a", "b", "c"])
```

## `operation` + `=`
```python
x = 0
x += 1
x *= 2
x **= 3
x %= 4
x /= 5
```

## Exercise
- Complete the two problems under List/String problems on [CodingBat](http://codingbat.com/home/konstans@stuy.edu/intro).
- Write your own `mySplit(strA, strB)` function that behaves exactly like the `split` method.
- Write your own `myJoin(str, list)` function that behaves exactly like the `join` method.
