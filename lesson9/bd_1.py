from random import randint
from time import sleep
# Создаём список из 1000 уникальных символов, исключая эмодзи, добавляя иероглифы

# Латиница (A-Z, a-z)
latin_upper = [chr(c) for c in range(65, 91)]
latin_lower = [chr(c) for c in range(97, 123)]

# Кириллица (А-Я, а-я)
cyrillic_upper = [chr(c) for c in range(1040, 1072)]
cyrillic_lower = [chr(c) for c in range(1072, 1104)]

# Греческие символы (α-ω)
greek = [chr(c) for c in range(945, 970)]

# Цифры
digits = [chr(c) for c in range(48, 58)]

# Пунктуация и спецсимволы
punctuation = list("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")

# Стрелки
arrows = [chr(c) for c in range(8592, 8602)]

# Технические символы (разные)
misc_symbols = [chr(c) for c in range(9728, 9743)] + [chr(c) for c in range(9750, 9760)]

# Математические операторы
math_symbols = [chr(c) for c in range(8704, 8736)]

# Валютные символы
currency_symbols = ['€', '©', '®', '™', '₸', '₽', '₩', '¥', '£', '$']

# Иероглифы (200 символов из CJK Unified Ideographs)
chinese_characters = [chr(c) for c in range(0x4E00, 0x4E00 + 200)]

# Объединяем всё
bd_txt = "С днём рождения!!!"
all_chars = (
    latin_upper + latin_lower +
    cyrillic_upper + cyrillic_lower +
    greek + digits +
    punctuation + arrows +
    misc_symbols + math_symbols +
    currency_symbols + chinese_characters
) + list(bd_txt)

# print(all_chars)

out_text = ""
pointer = 0
while True:
    rnum = randint(0, len(all_chars)-1)
    out_text += all_chars[rnum]
    print(out_text)
    out_text = out_text[:-1]
    if bd_txt[pointer] == all_chars[rnum]:
        out_text += all_chars[rnum]
        pointer += 1
    # print(out_text)
    if out_text == bd_txt:
        break
    sleep(0.005)
