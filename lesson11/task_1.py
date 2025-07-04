# исходный текст
txt = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
"""

# превращаем стих в список слов
words_list = txt.split()
print(words_list)

# удалить символы (, ; : .) с строках
for i in range(len(words_list)):
    words_list[i] = words_list[i].lower()
    words_list[i] = words_list[i].replace(":", "")
    words_list[i] = words_list[i].replace(",", "").replace(";", "")
    words_list[i] = words_list[i].replace(".", "")

print(words_list)
words_dictionary = {} # "Там": 6,

for word in words_list:
    if word in words_dictionary:
        words_dictionary[word] += 1
    else:
        words_dictionary[word] = 1
    
print(words_dictionary)
