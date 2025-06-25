field = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"],
]
winner = None
turn = "X"

# Цикл
while True:
    # Ввод
    print("Ход", turn)
    
    while True:
        x = int(input("Введите координату высоты: ")) # 2
        y = int(input("Введите координату широты: ")) # 1
        # МБ проверка
        if not ((0 <= x <= 2) and (0 <= y <= 2)):
            print("Нельзя")
            continue
        
        if field[x][y] != "_":
            print("Нельзя")
        else:
            break
    
    # Записать её в матрицу
    field[x][y] = turn
    
    # Обработка
    # Проверить что игра не окончена
    # 1. Три в ряд
    if field[0][0] == turn and field[0][1] == turn and field[0][2] == turn:
        winner = turn
    elif field[1][0] == turn and field[1][1] == turn and field[1][2] == turn:
        winner = turn
    # to do
    # ... Аиза, тут будет продолжение, вернёмся после рекламы
    
    # 2. Нет ходов
    q = 0
    for row in field:
        for cell in row:
            if cell != "_":
                q = q + 1
    
    if q == 9:
        print("Нет ходов")
        break
    
    # Проверка победителя
    if winner:
        print("Пабедилъ: ", turn)
        break
    
    # Вывод
    for line in field:
        print(line[0], line[1], line[2])
        
    # Смена хода
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
