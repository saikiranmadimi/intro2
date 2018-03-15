```python
def hasThreeCaps(s):
  x = 0
  while x < len(s) - 2:
    if s[x: x + 3].upper() == s[x: x + 3]:
      return True
    x = x + 1
  return False
```
