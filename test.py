lst = [4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5]

checkNumber = lst.pop()
multipliedDigits = [int(i) * 2 for i in lst[::2]]
subtractedDigits = [x - 9 for x in multipliedDigits if x > 9]
secondDigit = str(sum(subtractedDigits) + sum(multipliedDigits[1::2]))[1]



print(sum(subtractedDigits))
print(sum(multipliedDigits[1::2]))
print(secondDigit)
print(checkNumber)
