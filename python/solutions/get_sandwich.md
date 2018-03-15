# Get Sandwich
You have to identify the first occurrence and last occurrence of `bread`. In order to find the last occurrence, you can reverse the string and search for `daerb`. Once you have the positions, you need to offset the positions by 5 to account for the length of the word.
```python
def getSandwich(s):
  output = ""
  if s.count("bread") >= 2:
    first = s.find("bread")
    last = len(s) - s[::-1].find("daerb")
    output = s[first+5:last-5]
  return output
```
