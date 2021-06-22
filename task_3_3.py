def thesaurus(*user_names):
    names_dict = {}
    for name in user_names:
        if isinstance(name, str) == True:
            first_letter = name[0].upper()
            if first_letter not in list(names_dict.keys()):
                names_dict[first_letter] = [name]
            else:
                names_dict[first_letter].append(name)

    sorted_keys = sorted(names_dict, key=names_dict.get)
    print(sorted_keys)

    sorted_names_dict = {}
    for key in sorted_keys:
        sorted_names_dict[key] = names_dict[key]

    # print(names_dict)
    print(sorted_names_dict)

thesaurus("Иван", "Мария", "Петр", "Илья", "Анастасия")