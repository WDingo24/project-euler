from itertools import permutations, chain
from funcs import isPrime

pandigtals = chain.from_iterable(map(lambda x: int("".join(map(str, x))), permutations(range(1, y))) for y in range(2, 11))
print(max([num for num in pandigtals if isPrime(num)]))