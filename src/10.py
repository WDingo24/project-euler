from funcs import primeNumbers

itr = primeNumbers()
total = 0
while True:
    this = next(itr)
    if this >= 2000000:
        break
    total += this
print(total)