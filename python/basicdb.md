# Basic Databases

## Apple Stock Prices
Suppose we could access yesterday's stock prices as a list, where:

The indices are the time in minutes past trade opening time, which was 9:30am local time.
The values are the price in dollars of Apple stock at that time.
So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

```python
stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
get_max_profit(stock_prices_yesterday)
# Returns 6 (buying for $5 and selling for $11)
```

## Current Events - Cambridge Analytica
1) [Cambridge Analytica](https://www.nytimes.com/2018/04/12/technology/privacy-researchers-facebook.html)
2) [Mark Zuckerberg](https://www.nytimes.com/2018/04/12/technology/mark-zuckerberg-testimony.html)


## Solutions
Element Count
```python
def elementcount(arr):
    output = []
    for el in arr:
        if len(output) == 0:
            output.append([1, el])
        else:
            if el == output[-1][-1]:
                output[-1][0] += 1
            else:
                output.append([1, el])
    return output
```
Locker Problem
```python
def lockerz():
    x = 0
    lockers = []
    while x < 100:
        lockers.append(True)
        x += 1
    for num in range(2, 101):
        y = num
        while y <= 100:
            lockers[y - 1] = not lockers[y - 1]
            y += num
    output = []
    for idx, locker in enumerate(lockers):
        if locker:
            output.append(idx + 1)
    return output
```
Remove Duplicates
```python
def removeDups(arr):
  output = []
  for el in arr:
    if el not in output: # the in keyword loops through the output array
      output.append(el)
  return output
```
