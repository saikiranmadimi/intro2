# Centered Average

```python
def myMax(nums):
  big = nums[0]
  idx = 0
  while idx < len(nums):
    if nums[idx] >= big:
      big = nums[idx]
    idx = idx + 1
  return big

def myMin(nums):
  small = nums[0]
  idx = 0
  while idx < len(nums):
    if nums[idx] <= small:
      small = nums[idx]
    idx = idx + 1
  return small

def centered_average(nums):
  idx = 0
  output = 0
  while idx < len(nums):
    output = output + nums[idx]
    idx = idx + 1
  return (output - myMax(nums) - myMin(nums)) / (len(nums) - 2)
```
