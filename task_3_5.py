from random import choice, sample

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(count, repeat=True):
    ''' Введите количество шуток и получите список фраз и трех слов'''
    try:
        count = int(count)
        if count <= 0:
            print('Столько шуток не бывает')

        else:
            if repeat == True:
                n = 1
                phrase_list = []
                while n <= count:
                    phrase_list += [' '.join([choice(nouns), choice(adverbs), choice(adjectives)])]
                    n += 1
                print(phrase_list)
            else:
                if count > len(nouns):
                    print(f"Простите, но без повторения слов могу составить только {len(nouns)} шуток")
                else:
                    phrase_list = []
                    for noun, adverb, adjective in zip(sample(nouns, count), sample(adverbs, count), sample(adjectives, count)):
                        phrase_list += [' '.join([noun, adverb, adjective])]
                    print(phrase_list)

    except ValueError:
        print('Не шутите с вводом данных!')

if __name__ == "__main__":
    help(get_jokes)

    get_jokes(2)
    get_jokes("5")
    get_jokes("qwerty")
    get_jokes("0")
    get_jokes(-3)

    get_jokes(5, repeat=False)
    get_jokes(6, repeat=False)
    get_jokes(0, repeat=False)