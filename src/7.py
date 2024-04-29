from funcs import primeList

print(next(x for i,x in enumerate(primeList()) if i==10000))