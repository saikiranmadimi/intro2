# Problem 1: 233168
```python
def mult35():
    sum = 0
    x = 0
    while x < 1000:
        if x % 3 == 0:
            sum += x
        elif x % 5 == 0:
            sum += x
        x += 1
    return sum
```

# Problem 2: 4613732
```python
def bigFib():
    a, b = 1, 2
    sum = 0
    while b < 4000000:
        if b % 2 == 0:
            sum += b
        a, b = b, (a + b)
    return sum
```

# Problem 3: 6857
```python
def isPrime(n):
    for num in range(2, int(n**(.5) + 1)):
        if n % num == 0:
            return False
    return True

def largePrimeFactor(n):
    lpf = 2
    while not isPrime(n):
        if isPrime(lpf) and n % lpf == 0:
            n /= lpf
        lpf += 1
    return n

```

# Problem 4: 906609
```python
def isPalindrome(num):
    num = str(num)
    return num == num[::-1]

def findBigP():
    x = 0
    output = 0
    while x < 1000:
        y = 0
        while y < 1000:
            if isPalindrome(x * y) and x * y > output:
                output = x * y
            y += 1
        x += 1
    return output
```

# Problem 5: 232792560
```python
def gcf(a, b):
    if b == 0:
        return a
    return gcf(b, a % b)

def lcm(a, b):
    return a * b / gcf(a, b)

def lcm20():
    x = 1
    output = 1
    while x < 21:
        output = lcm(output, x)
        x += 1
    return output
```

# Problem 6: 25164150
```python
def sumsquarediff():
    sumSquares = 0
    sum = 0
    x = 1
    while x < 101:
        sumSquares += x ** 2
        sum += x
        x += 1
    return (sum ** 2) - sumSquares
```

# Problem 7: 104743
```python
def isPrime(n):
    for num in range(2, int(n**(.5) + 1)):
        if n % num == 0:
            return False
    return True

def prime10001():
    count = 0
    x = 2
    while count < 10001:
        if isPrime(x):
            count += 1
        x += 1
    return x - 1

```

# Problem 8: 23514624000
```python
def strToProduct(str):
    x = 0
    product = 1
    while x < len(str):
        product *= int(str[x])
        x += 1
    return product

def findProduct13():
    bignum = "73167176531330624919225119674426574742355349194934969835203127745063262395783180169848018694788518438586156078911294949545950173795833195285320880551112540698747158523863050715693290963295227443043557668966489504452445231617318564030987111217223831136222989342338030813533627661428280644448664523874930358907296290491560440772390713810515859307960866701724271218839987979087922749219016997208880937766572733300105336788122023542180975125454059475224352584907711670556013604839586446706324415722155397536978179778461740649551492908625693219784686224828397224137565705605749026140797296865241453510047482166370484403199890008895243450658541227588666881164271714799244429282308634656748139191231628245861786645835912456652947654568284891288314260769004224219022671055626321111109370544217506941658960408071984038509624554443629812309878799272442849091888458015616609791913387549920052406368991256071760605886116467109405077541002256983155200055935729725716362695618826704282524836008232575304207529634"
    x = 0
    largestProduct = 0
    while x < len(bignum) - 13:
        sliced = bignum[x:x+13]
        if strToProduct(sliced) > largestProduct:
            largestProduct = strToProduct(sliced)
        x += 1
    return largestProduct
```

# Problem 9: 31875000
```python
def pyth1000():
    a = 1
    while a < 300:
        b = a + 1
        while b < 500:
            c = ((a ** 2) + (b ** 2)) ** 0.5
            if a + b + c == 1000.0:
                return [a, b, c]
            b += 1
        a += 1
```

# Problem 10: 142913828922
```python
def milli():
    x = 3
    sum = 0
    while x < 2000000:
        if isPrime(x):
            sum += x
        x += 2
    return sum + 2
```
