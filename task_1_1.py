def count_period(duration):
    if duration < 60 and duration >=0: #меньше минуты
        print(f"Продолжительность периода составляет {duration} секунд")
    elif duration >= 60 and duration <3600: #меньше часа
        minuits = duration//60
        seconds = duration%60
        print(f"Продолжительность периода составляет {minuits} минут и {seconds} секунд")
    elif duration >=3600: #Больше часа
        hours = duration // 3600
        minuits = (duration - hours*3600) // 60
        seconds = (duration - hours*3600 - minuits*60) % 60
        if hours <24:
            print(f"Продолжительность периода составляет {hours} часов {minuits} минут и {seconds} секунд")
        elif hours >24:
            days = hours//24
            hours = hours%24
            if days <7:
                print(f"Продолжительность периода составляет {days} суток {hours} часов {minuits} минут и {seconds} секунд")
            elif days >= 7 and days<365:
                weeks = days//7
                days = days%7
                print(f"Продолжительность периода составляет {weeks} недель {days} суток {hours} часов {minuits} минут и {seconds} секунд")
            elif days >=365:
                years = days//365
                weeks = (days%365)//7
                days = (days%365)%7
                print(
                    f"Продолжительность периода составляет {years} год {weeks} недель {days} суток {hours} часов {minuits} минут и {seconds} секунд")

while True:
    try:
        duration = input('Введите длительность в секундах: ')
        duration = int(duration)
        count_period(duration)
        break

    except ValueError:
        print("Неверный формат")
