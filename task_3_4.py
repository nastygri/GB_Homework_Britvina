def thesaurus_adv(*user_names):
    names_dict = {}
    for full_name in user_names:
        name, surname = full_name.split(' ')
        first_letter_surname = surname[0].upper()
        first_letter_name = name[0].upper()
        if first_letter_surname not in list(names_dict.keys()):
            names_dict[first_letter_surname] = {}
            names_dict[first_letter_surname][first_letter_name] = [full_name]
        else:
            if first_letter_name not in list(names_dict[first_letter_surname].keys()):
                names_dict[first_letter_surname][first_letter_name] = [full_name]
            else:
                names_dict[first_letter_surname][first_letter_name].append(full_name)

    sorted_names_dict = sort_dict_foo(names_dict)
    deep_sorted_names_dict = {}
    for key, inner_dict in sorted_names_dict.items():
        deep_sorted_names_dict[key] = sort_dict_foo(inner_dict)

    # print(names_dict)
    # print(sorted_names_dict)
    print(deep_sorted_names_dict)


def sort_dict_foo(user_dict):
    # Почему-то не сработало:
    # sorted_keys = sorted(user_dict, key=user_dict.get)
    # Пришлось сделать вот так:
    keys = list(user_dict.keys())
    sorted_keys = sorted(keys)
    sorted_dict = {}

    for key in sorted_keys:
        sorted_dict[key] = user_dict[key]

    return sorted_dict


thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")