totDays = sum([366 if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 365 for year in range(1901, 2001)])
sundays = [x for x in range(1, totDays+1) if x % 7 == 1]
firsts = []
days = 1
for year in range(1901, 2001):
    months = [31, 29 if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for month in months:
        firsts.append(days)
        days += month
print(len(set(sundays).intersection(set(firsts))))