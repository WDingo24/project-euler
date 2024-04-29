for a in range(1, 999):
    for b in range(1, 999):
        if a**2+b**2 == (1000-(a+b))**2:
            print(a, b, 1000-(a+b), a*b*(1000-(a+b)))