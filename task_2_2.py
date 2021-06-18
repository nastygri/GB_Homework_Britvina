task = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# Создаем список элементов с кавычками и с форматированным числом
count = 0
while count < len(task):
     try:
         int_item = int(task[count])

         if '+' in task[count]:
             # new_item = f'"+{int_item:02d}"'
             new_item = f'+{int_item:02d}'
         elif '-' in task[count]:
             # new_item = f'"-{int_item:02d}"'
             new_item = f'-{int_item:02d}'
         else:
             # new_item = f'"{int_item:02d}"'
             new_item = f'{int_item:02d}'

         task[count] = new_item
         task.insert(count, '"')
         task.insert(count + 2, '"')
         count += 3

     except ValueError:
        count += 1

print(task)

# Соединяем все в строку
final_line = ''
for i, item in enumerate(task):
    if item == '"':
        # Если после кавычки число - прибавлять без пробела. Иначе - с пробелом.
        try:
            _int_item = int(task[i + 1])
            final_line += item
        except ValueError:
            final_line += item + ' '
    else:
        try:
            # Если элемент является числом
            _int_item = int(item)
            # и после этого идут кавычки - прибавлять без пробела. Иначе - с пробелом.
            if task[i + 1] == '"':
                final_line += item
            else:
                final_line += item + ' '
        # Если элемент не является числом - прибавлять с пробелом.
        except ValueError:
            final_line += item + ' '


print(final_line)




