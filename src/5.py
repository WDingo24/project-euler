i = 2520
while True:
    if not any([i % x for x in range(1, 21)]):
        print(i)
        break
    i += 2520