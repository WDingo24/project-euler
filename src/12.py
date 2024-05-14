from math import sqrt
from funcs import divisors

base = 1
tri = 0
while True:
    tri += base
    if len(list(divisors(tri))) > 500:
        print(tri)
        break
    base += 1