from funcs import isPrime
from itertools import product

highest = 0
coefs = (0, 0)
for a, b in product(range(-1000, 1001), repeat=2):
    if a == 1000 or a == -1000:
        continue
    n = 0
    while isPrime((n**2)+(a*n)+b):
        n += 1
    if n > highest:
        highest = n
        coefs = (a, b)
print(coefs[0]*coefs[1])