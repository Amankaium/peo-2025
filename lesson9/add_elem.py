profile = {
    "name": "Gulaiym",
    "age": 20,
    "code": ["Python", "SQL"],
}

n = int(input("Сколько элементов хотите добавить? "))

for i in range(n):
    new_key = input("Введите ключ: ")
    new_value = input("Введите значение: ")
    profile[new_key] = new_value
    
print(profile)