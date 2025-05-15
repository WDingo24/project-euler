from funcs import primeNumbers, isPrime

primes = primeNumbers()
trunc = []

while n := next(primes):
    if n < 8:
        continue
    if len(trunc) == 11:
        break
    string  = str(n)
    if set(map(int, string)).intersection(set(range(4,10,2))):
        continue
    if all([isPrime(int(string[:i])) and isPrime(int(string[i:])) for i in range(1, len(string))]+[n]):
        print(string)
        trunc.append(n)

print(sum(trunc))