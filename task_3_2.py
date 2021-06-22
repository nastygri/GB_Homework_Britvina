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

def num_translate_adv(number):
    if isinstance(number, str):
        try:
            answer = translate_dict[number.lower()]
            if number[0].isupper() == True:
                print(answer[0].upper() + answer[1:].lower())
            else:
                print(answer)
        except KeyError:
            return None
    else:
        return None

num_translate_adv('One')
num_translate_adv('SeVen')
num_translate_adv('nine')
num_translate_adv('twelve')
num_translate_adv(12)