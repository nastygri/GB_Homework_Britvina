import requests
import datetime


def currency_rates(user_currency):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    r = requests.get(url)

    current_date_str = r.text.split('Date="')[1][:10]
    current_date_list = list(map(int, current_date_str.split('.')))
    current_date = datetime.date(year=current_date_list[2], month=current_date_list[1], day=current_date_list[0])

    currencies = r.text.split('Valute ID=')
    currencies_dict = {}
    for currency in currencies[1:]:
        code = currency.split('CharCode')[1][1:-2]
        value = (currency.split('Value')[1][1:-2])
        value = float(value.replace(',', '.'))
        currencies_dict[code] = value

    user_currency = user_currency.upper()

    if user_currency in list(currencies_dict.keys()):
        return currencies_dict[user_currency], current_date


if __name__ == '__main__':
    print(currency_rates("EUR"))
    print(currency_rates("usd"))
    print(currency_rates("daf"))