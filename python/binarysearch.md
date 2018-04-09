# Binary Search
The binary search algorithm searches for an item in the same exact way you try and find a word in a physical dictionary. It works under the assumption that what you're searching through has already been sorted.

## Do Now
Think of 3 different systematic ways you can try to find a word in a dictionary. Which of the three is the most efficient or fastest? Which of the three is the least efficient or slowest?

## Steps
1) Break up the array into two halves: a left half and a right half
2) Check the item in the middle of the array
3) If the middle element is greater than what we're looking for, then search the left half
4) If the middle element is less than what we're looking for, then search the right half
5) Keep breaking the array in half until it can't be broken anymore

## Example 1
Let us say we are looking for the number `12` in the array below. You can choose to split the array up into 3 parts - left, middle, and right.
```python
bSearch([1, 2, 3, 4, 5, 7, 9, 12, 15, 18, 23]) #first recursive call
bSearch([9, 12, 15, 18, 23]) #second recursive call
bSearch([9, 12]) #third recursive call
```

## Example 2
Let us say we are looking for the number `12` in the array below. You can also just split the array into two halves.
```python
bSearch([1, 2, 3, 4, 5, 7, 9, 12, 15, 18, 23])
bSearch([7, 9, 12, 15, 18, 23])
bSearch([9, 12])
```
