profile = {
    "name": "Gulaiym",
    "age": 20,
    "code": "Python",
}
print(profile)
profile["company"] = "Red Petroleum" # добавление
print(profile)

del profile["age"]
print(profile)
profile["code"] = [profile["code"], "SQL"] # ["Python", "SQL"]
print(profile)

a = "hello"
a = [a, "world"]
print(a)