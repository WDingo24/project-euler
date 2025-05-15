from functools import reduce
from operator import mul

nonTrivial = []
for den in range(10, 100):
    for num in range(10, den):
        expected = num/den
        overlap = set(str(den)).intersection(set(str(num)))
        if not (num % 10 or num % 10):
            continue
        if len(overlap) == 1:
            print(den)
            char = overlap.pop()
            den_ = int(str(den).replace(char, "", 1))
            num_ = int(str(num).replace(char, "", 1))
            if den_ == 0:
                continue
            if num_/den_ == expected:
                nonTrivial.append((num, den))
fnum = reduce(mul, map(lambda x: x[0], nonTrivial))
fden = reduce(mul, map(lambda x: x[1], nonTrivial))
print(fden/fnum)