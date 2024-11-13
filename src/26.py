decimals = []
for denom in range(2, 1000):
    numer = 10
    remainders = []
    remain = None
    length = 0
    while remain not in remainders:
        if remain is not None:
            remainders.append(remain)
        length += 1
        remain = numer % denom
        numer = remain * 10
    decimals.append(length-1)

print(max(enumerate(decimals, 2), key=lambda x: x[1]))