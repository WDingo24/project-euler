from funcs import champernowne

tot = 1
powers = [10**n for n in range(7)]
seq = enumerate(champernowne())
i, digit = next(seq)
while i < 1000001:
    if i in powers:
        tot *= digit
    i, digit = next(seq)
print(tot)