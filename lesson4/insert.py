# создаётся переменная
# ввод данных
# форматирование в число
a = input("Введите а: ")        # "6"
if a.isnumeric():               # True
    print("Это число")          # V
    a = int(a)                  # 6
    b = float(input("Введите b: "))
    print("Сумма: ", a + b)
else:                           
    print("Нармална абшайся")
