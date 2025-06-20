a = int(input("Введите а: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))

# if a >= b and a >= c:
#     print(a)
# elif b >= a and b >= c:
#     print(b)
# else:
#     print(c)

# m - max
if a > b:
    if a > c:
        m = a 
    else:
        m = c
else:
    if b > c:
        m = b
    else:
        m = c

print(m)
