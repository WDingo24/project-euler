from itertools import permutations

perms = enumerate(permutations(range(0, 10)), 1)
while (tpl := next(perms))[0] != 1000000: continue
print(int("".join(map(str, tpl[1]))))