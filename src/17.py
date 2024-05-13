digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
total = 0
for x in range(1, 1001):
    if x < 10:
        total += len(digits[x-1])
    elif x > 10 and x < 20:
        total += len(teens[x-11])
    elif x < 100 and x % 10 == 0:
        total += len(tens[x//10-1])
    elif x < 100:
        ten = tens[int(str(x)[0])-1]
        digit = digits[int(str(x)[1])-1]
        total += len(ten+digit)
    elif x >= 100 and x != 1000:
        string = digits[int(str(x)[0])-1]+"hundred"
        ten = int(str(x)[1])
        digit = int(str(x)[2])
        if ten != 0 or digit != 0:
            string += "and"
        if ten != 0 and digit == 0:
            string += tens[ten-1]
        elif ten == 1:
            string += teens[digit-1]
        elif ten == 0 and digit != 0:
            string += digits[digit-1]
        elif ten != 0 and digit != 0:
            string += tens[ten-1]+digits[digit-1]
        total += len(string)
    else:
        total += len("onethousand")
print(total)