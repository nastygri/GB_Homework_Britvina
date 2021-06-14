list_numbers = []
for number in range(1,1000):
    if number%2 != 0:
        list_numbers.append(number**3)
print(list_numbers)

list_summs = []
for item in list_numbers:
    summ = 0
    for symbol in str(item):
        summ += int(symbol)
    if summ%7==0:
        list_summs += [item]


print(list_summs)


list_summs2 = []
for item in list(map(lambda x: x+17, list_numbers)):
    summ = 0
    for symbol in str(item):
        summ += int(symbol)
    if summ%7==0:
        list_summs2 += [item]

print(list_summs2)