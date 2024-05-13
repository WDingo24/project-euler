from funcs import primes

print(next(x for i,x in enumerate(primes()) if i==10000))