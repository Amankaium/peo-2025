print("hello")
a = len([7, 2, 6])
print(a)
profile = {
    "name": "Gulaiym",
    "age": 20,
    "code": ["Python", "SQL"],
}
b = len(profile)
print(b)

def sum_2(a, b):
    c = a + b
    return c

print(sum_2(7, 9)) # 16
print(sum_2(6, 4)) # 16
print(sum_2(2, 0)) # 16
print(sum_2(7, 9)) # 16
print(sum_2(7, 9)) # 16

num_1 = int(input())
num_2 = int(input())
print(sum_2(num_1, num_2))
