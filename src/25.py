from funcs import fibonacci

fib = fibonacci()
num = 0
i = 0
while len(str(num)) < 1000:
    num = next(fib)
    i += 1
print(i)