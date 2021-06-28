count = 5
odd_nums_gen = (i for i in range(0, count + 1) if i % 2 != 0)

print(next(odd_nums_gen), next(odd_nums_gen), next(odd_nums_gen))
print(odd_nums_gen)