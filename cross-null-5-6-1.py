# Создаю игровое поле
ROW = 4
COL = 4
matrix_x0 = [
    [' ', 0, 1, 2],
    [0, '-', '-', '-'],
    [1, '-', '-', '-'],
    [2, '-', '-', '-']
]

# функция вывода игрового поля в консоль
def print_matrix_x0():
    for i in range(ROW):
        for j in range(COL):
            print(matrix_x0[i][j], end = ' ')
        print()

# Функция для ввода игроком хода
def enter_step(matrix_x0, symbol):
    while True:
        print('Ходит игрок', symbol)
        index_i = input('Введите строку: ')
        index_j = input('Введите столбец: ')
        if index_i not in '012' or index_j not in '012':
            print('Вы ввели неверные данные. Попробуйте еще раз.')
            continue
        else:
            index_i, index_j = int(index_i), int(index_j)
            if matrix_x0[index_i+1][index_j+1] == '-':
                matrix_x0[index_i+1][index_j+1] = symbol
                break
            else:
                print('Ячейка занята, попробуйте еще раз')
                continue

import numpy as np

# Создаем функцию для определения победителя
def check_win():
    winner = ''
    g_1, g_2, g_3 = [], [], []
    v_1, v_2, v_3 = [], [], []
    d_1, d_2 = [], []

    m = np.array(matrix_x0)
    v_1 = list(m[1:, 1])
    v_2 = list(m[1:, 2])
    v_3 = list(m[1:, 3])

    g_1 = matrix_x0[1][1:]
    g_2 = matrix_x0[2][1:]
    g_3 = matrix_x0[3][1:]
    d_1 = [matrix_x0[1][1], matrix_x0[2][2], matrix_x0[3][3]]
    d_2 = [matrix_x0[1][3], matrix_x0[2][2], matrix_x0[3][1]]
    x = ['X', 'X', 'X']
    o = ['0', '0', '0']
    if any([g_1 == x,
            g_2 == x,
            g_3 == x,
            d_1 == x,
            d_2 == x,
            v_1 == x,
            v_2 == x,
            v_3 == x]):
        winner = 'X'
    elif g_1 == o or g_2 == o or g_3 == o or d_1 == o or d_2 == o or v_1 == o or v_2 == o or v_3 == o:
        winner = '0'
    return winner


symbol = 'X'
winner = None
step = 0
print_matrix_x0()
while True:
    step += 1
    if step % 2 == 0:
        player = '0'
    else:
        player = 'X'
    enter_step(matrix_x0, player)
    print_matrix_x0()
    winner = check_win()
    if winner:
        print('Победил', winner, '! Игра окончена!')
        break
    if step == 9:
        print('Ничья! Победила дружба!')
        break

