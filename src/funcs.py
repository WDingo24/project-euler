from typing import Generator
from math import sqrt, factorial
from itertools import cycle

def divisors(n: int) -> Generator:
    for x in range(1, int(sqrt(n))+1):
        if n % x == 0:
            yield x
            if x != 1 and x != sqrt(n):
                yield n//x

def primeNumbers() -> Generator:
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

def collatz(start: int) -> Generator:
    yield start
    while start != 1:
        if start % 2 == 0:
            start = start // 2
            yield start
        else:
            start *= 3
            start += 1
            yield start

def fibonacci(start: tuple=(1, 0)) -> Generator:
    a, b = start
    while True:
        a, b = b, a + b
        yield b

def choice(n: int, k: int) -> float:
    return factorial(n) / (factorial(k) * factorial(n-k))

def amicableNumbers() -> Generator:
    num = 1
    while True:
        divSum = sum(divisors(num))
        if divSum != num and num == sum(divisors(divSum)):
            yield num
        num += 1

def abundantNumbers() -> Generator:
    num = 12
    while True:
        if sum(divisors(num)) > num:
            yield num
        num += 1

def isPrime(num: int) -> bool:
    if num == 1:
        return False
    if num in (2, 3):
        return True
    if not num % 2 or num < 0:
        return False
    for i in range(3, int(sqrt(num))+1, 2):
        if not num % i:
            return False
    return True

def champernowne() -> Generator:
    num = 0
    while True:
        for char in str(num):
            yield int(char)
        num += 1

def A316667_VF(end: int) -> Generator:
    moves = [
        lambda x, y: (x+1, y),
        lambda x, y: (x, y-1),
        lambda x, y: (x-1, y),
        lambda x, y: (x, y+1)
    ]

    moveGen = cycle(moves)
    n = 1
    pos = 0, 0
    times = 1

    yield n, pos

    while True:
        for _ in range(2):
            move = next(moveGen)
            for _ in range(times):
                if n >= end:
                    return
                pos = move(*pos)
                n += 1
                yield n, pos
        times += 1