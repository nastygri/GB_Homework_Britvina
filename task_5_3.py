tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Петр', 'Алексей', 'Иван'
]

klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

if len(tutors) > len(klasses):
    none_classes_count = len(tutors) - len(klasses)
    for i in range(none_classes_count):
        klasses.append(None)

gen = ((tutor, klass) for tutor, klass in zip(tutors, klasses))

print(type(gen))
for i in range(len(tutors)):
    print(next(gen))