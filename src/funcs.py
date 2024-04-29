from math import sqrt

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