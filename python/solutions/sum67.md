# Sum67
You can solve this problem by creating a variable that stores whenever you've encountered a six. By setting it to a boolean, you make your life easier. While the boolean value is `True`, you'll disregard values. When you encounter a seven, it'll reset the boolean to `False` and you'll continue incorporating values into the output.
```python
def sum67(nums):
  seenSix = False
  idx = 0
  output = 0
  while idx < len(nums):
    if nums[idx] == 6:
      seenSix = True
    if not seenSix:
      output = output + nums[idx]
    if nums[idx] == 7 and seenSix:
      seenSix = False
    idx = idx + 1

  return output
```
