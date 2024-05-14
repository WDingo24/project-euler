from funcs import primeNumbers

print(next(x for i,x in enumerate(primeNumbers()) if i==10000))