bad_boys = ["Илим", "Бакберди", "Тилек"]
# index      0          1           2

girls = [
    "Гулайым",
    "Айзат",
    "Айжан",
    "Аиза"
]

print(bad_boys[1])          # чтение 1 элемента
bad_boys.append("Бакыт")    # добавление в конец
print(bad_boys)             # чтение всего списка
bad_boys[0] = "Илимбек"     # изменение 1 значения
print(bad_boys) 
del bad_boys[2]             # удаление 1 элемента
print(bad_boys)

bad_boys[0], bad_boys[2] = bad_boys[2], bad_boys[0]
print(bad_boys)

print(bad_boys[0])
print(bad_boys[1])
print(bad_boys[2])

for i in range(len(girls)):
    print(i)
