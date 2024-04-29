from math import sqrt

base = 1
tri = 0
while True:
    tri += base
    factors = []
    for x in range(1, int(sqrt(tri))+1):
        if x == int(sqrt(tri)):
            factors.append(x)
        elif not tri % x:
            factors += [x, tri/x]
    if len(factors) > 500:
        print(tri)
        break
    base += 1