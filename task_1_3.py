def foo(number):
    if number == 1:
        print(f'1 процент')
    elif number in [2,3,4]:
        print(f'{number} процента')
    elif number >=5 and number<= 20:
        print(f'{number} процентов')
    else:
        print("Вы ввели число не в промежутке от 1 до 20")

while True:
    try:
        number = int(input("Введите число от 1 до 20: "))
        foo(number)

    except ValueError:
        break

#Проверка всех склонений после выхода из цикла
for item in range(1,21):
    foo(item)
 #проверка
