lst = []
for x in range(999, 99, -1):
    for y in range(999, 99, -1):
        z = x * y
        if str(z) == "".join(reversed(str(z))):
            lst.append(z)
print(max(lst))
