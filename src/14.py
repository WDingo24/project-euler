from funcs import collatz

highest = 0
num = 0
for x in range(1, 1000001):
    length = sum(1 for _ in collatz(x))
    if length > highest:
        highest = length
        num = x
print(num)