from funcs import abundantNumbers
from itertools import takewhile, combinations_with_replacement

nums = set(range(1, 28124))
abundants = takewhile(lambda x: x<28124, abundantNumbers())
sums = set(map(sum, combinations_with_replacement(abundants, 2)))
print(sum(nums-sums))