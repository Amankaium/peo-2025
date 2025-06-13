# Ввод
age = int(input("Введите возраст: "))
has_ticket = input("Есть ли билет? (Да\Нет): ") # "Нет" == "Да"
if has_ticket != "Да" or has_ticket != "Нет":
    print("Неверный ввод, попробуйте ещё раз (допустимые значения: Да или Нет)")
    has_ticket = input("Есть ли билет? (Да\Нет): ")
has_ticket = has_ticket == "Да" # or has_ticket == "Yes" or has_ticket == "Ооба"

min_height = 100 # по регламенту
child_height = int(input("Введите рост: ")) # частный случай, факт

# Обработка
if age < 6 and min_height < child_height:
    message = "Проходит бесплатно"
elif has_ticket and min_height < child_height:
    message = "Проходит"
else:
    message = "Не проходит"

# Вывод
print(message)
