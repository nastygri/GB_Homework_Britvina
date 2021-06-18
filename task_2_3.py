task = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# print(id(task))

for i, item in enumerate(task):
    try:
        int_item = int(item)
        #task.insert(i, '"')

        if '+' in item:
            new_item = f'"+{int_item:02d}"'
        elif '-' in item:
            new_item = f'"-{int_item:02d}"'
        else:
            new_item = f'"{int_item:02d}"'
        task[i] = new_item

    except ValueError:
        pass

# print(id(task))

print(" ".join(task))

