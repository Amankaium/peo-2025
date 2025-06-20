a = int(input("Введите а: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
d = int(input("Введите d: "))
m = a
if a > b:
    if a > c:
        if a > d:
            m = a
        else:
            m = d
    else:
        if c > d:
            m = c
        else:
            m = d
else:
    if b > c:
        if b > d:
            m = b
        else:
            m = d
    else:
        if c > d:
            m = c
        else:
            m = d

print(m)        
