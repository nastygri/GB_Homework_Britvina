translate_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

def num_translate(number):
    try:
        print(translate_dict[number])
    except KeyError:
        return None

num_translate('one')
num_translate('seven')
num_translate('twelve')

