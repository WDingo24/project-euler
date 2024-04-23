seq = [1, 2]
while seq[-1] < 4000000:
    seq.append(seq[-2] + seq[-1])
print(sum(list(filter(seq, lambda x: not x % 2))))