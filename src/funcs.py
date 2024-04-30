from math import sqrt, factorial

def primeList():
    yield 2
    num = 1
    while True:
        num += 2
        prime = True
        for i in range(3, int(sqrt(num))+1, 2):
            if not num % i:
                prime = False
        if prime:
            yield num

def collatz(start):
    yield start
    while start != 1:
        if start % 2 == 0:
            start = int(start / 2)
            yield start
        else:
            start *= 3
            start += 1
            yield start

def choice(n, k):
    return factorial(n) / (factorial(k) * factorial(n-k))