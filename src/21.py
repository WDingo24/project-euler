from funcs import amicableNumbers

total = 0
amicables = amicableNumbers()
num = next(amicables)
while num < 10000:
    total += num
    num = next(amicables)
print(total)