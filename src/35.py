from funcs import isPrime

circular = {2,}
checked = set()

for x in range(3, 1000001, 2):
    hasEven=False
    if x in circular:
        continue
    for digit in str(x):
        if not int(digit) % 2:
            hasEven = True
    if hasEven:
        continue
    x = str(x)
    nums = {int(x[i:]+x[:i]) for i in range(len(x))}
    if all(isPrime(num) for num in nums):
        for num in nums:
            circular.add(num)

print(len(circular))