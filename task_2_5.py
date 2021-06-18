prices = [57.8, 46.51, 97, 33.4, 456.87, 123.0, 45, 7945.66, 943.2, 3642.94]

for i, price in enumerate(prices):
    price = str(float(price))
    rub, cent = price.split('.')
    line = f'{rub} руб {int(cent):02d} коп'
    if i != len(prices) - 1:
        print(line, end =", ")
    else:
        print(line)

print("Цены по возростанию, список тот же:")
print(id(prices))
prices.sort()
print(prices)
print(id(prices))

print("Цены по убыванию, список другой:")
print(id(prices))
prices_sorted = list(sorted(prices, reverse = True))
print(prices_sorted)
print(id(prices_sorted))

print("5 дорогих товаров, цены по возростанию:")
prices_5_max = list(sorted(prices))[-5:]
print(prices_5_max)