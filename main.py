
field = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]   # создание поля для игры
win_comb = [((0, 0), (0, 1), (0, 2)),
            ((1, 0), (1, 1), (1, 2)),
            ((2, 0), (2, 1), (2, 2)),
            ((0, 2), (1, 1), (2, 0)),
            ((0, 0), (1, 1), (2, 2)),
            ((0, 0), (1, 0), (2, 0)),
            ((0, 1), (1, 1), (2, 1)),
            ((0, 2), (1, 2), (2, 2))] # случаи выигрыша

count = 0 # переменная для x или 0

def coords():
    print(' ','0', '1', '2')# Вывод в консоль поля
    for i in range (3):
        print(i, field[i][0], field[i][1], field[i][2])

coords()

def user_chose(): # выбор крестика или нолика
    while True: # прервётся в конце игры
        x = int((input('Впишите X (от 0 до 2) ')))
        y = int((input('Впишите Y (от 0 до 2) ')))

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Неверные координаты")
            continue

        if field[x][y] != " ":
            print("Клетка занята")
            continue

        return x, y



def win_loose():
    for i in win_comb: # При i = 0, берёт ((0, 0), (0, 1), (0, 2)); i = 1 ((1, 0), (1, 1), (1, 2)) и т.д
       c_1 = i[0] # при i = 0 (0, 0); i = 1 (1, 0);
       c_2 = i[1] # при i = 0 (0, 1); i = 1 (1, 1);
       c_3 = i[2] # при i = 0 (0, 2); i = 1 (1, 2);

       if field[c_1[0]][c_1[1]] == field[c_2[0]][c_2[1]] == field[c_3[0]][c_3[1]] != ' ':  # горизонт 1
           print('Выиграл ', field[c_1[0]][c_1[0]])
           return True

    return False

win_loose()


while True: # сам игровой процесс
    print('1-ый ходит X, 2-ой O')
    coords()

    x, y = user_chose()

    count += 1
    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if win_loose() == True:
        break

    elif count == 9:
        print("Ничья")
        break



