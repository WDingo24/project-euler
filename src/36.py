total = 0
for num in range(1, 1000000):
    string = str(num)
    if string == string[::-1]:
        binary = f"{num:b}"
        if binary == binary[::-1]:
            total += num
print(total)