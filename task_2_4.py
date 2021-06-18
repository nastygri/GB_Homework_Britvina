task = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for item in task:
    name = item.split(' ')[-1].lower()
    name = name[0].capitalize() + name[1:]
    print(f'Привет, {name}!')