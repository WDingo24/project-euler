from funcs import fibonacci

fib = enumerate(fibonacci())
num = 0
while len(str(num)) < 1000:
    i, num = next(fib)
print(i)