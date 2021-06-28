src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

'''
new_list = []
new_set = set()
for x in src:
    if x not in new_set and not new_set.add(x): 
    # not new_set.add(x) всегда дает True, используется только чтобы после проверки на наличие элемена в множестве 
    # - добавить его  туда 
        new_list.append(x)

print(new_list)
'''
new_set = set()
result = [x for x in src if x not in new_set and not new_set.add(x)]
print(result)