import random


# Функция для создания игрового поля
def create_board(size):
    board = [[' ' for _ in range(size)] for _ in range(size)]
    return board


# Функция для отображения игрового поля
def display_board(board):
    size = len(board)
    for row in board:
        print(' | '.join(row))
        print('-' * (4 * size - 1))


# Функция для проверки выигрышной комбинации
def check_winner(board, player):
    size = len(board)

    # Проверка по горизонтали и вертикали
    for i in range(size):
        if all(board[i][j] == player for j in range(size)):
            return True
        if all(board[j][i] == player for j in range(size)):
            return True

    # Проверка по диагоналям
    if all(board[i][i] == player for i in range(size)):
        return True
    if all(board[i][size - 1 - i] == player for i in range(size)):
        return True

    return False


# Функция для хода игрока
def player_move(board, player):
    while True:
        try:
            print("Ход игрока", player)
            row = int(input("Введите номер строки: ")) - 1
            col = int(input("Введите номер столбца: ")) - 1
            if row < 0 or row >= len(board) or col < 0 or col >= len(board):
                raise ValueError
            if board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("Выбранная ячейка уже занята!")
        except ValueError:
            print("Некорректный ввод! Введите целое число от 1 до", len(board))


# Функция для хода компьютера
def computer_move(board, player, difficulty):
    size = len(board)

    if difficulty == 'обычный':
        while True:
            row = random.randint(0, size - 1)
            col = random.randint(0, size - 1)
            if board[row][col] == ' ':
                board[row][col] = player
                break

# Функция для запуска игры
def play_game():
    print("Добро пожаловать в игру Крестики-нолики!")

    size = int(input("Выберите размер игрового поля: "))
    # Выбор режима игры
    while True:
        mode = input("Выберите режим игры (1 - один игрок, 2 - два игрока): ")
        if mode == '1' or mode == '2':
            break
        else:
            print("Некорректный ввод! Введите 1 или 2.")


    # Инициализация игрового поля
    board = create_board(size)

    # Основной игровой цикл
    current_player = 'X'
    difficulty = 'обычный'
    while True:
        display_board(board)

        if mode == '1' and current_player == 'O':
            computer_move(board, current_player, difficulty)
        else:
            player_move(board, current_player)

        if check_winner(board, current_player):
            display_board(board)
            print("Игрок", current_player, "победил!")
            break

        if all(board[i][j] != ' ' for i in range(size) for j in range(size)):
            display_board(board)
            print("Ничья!")
            break

        current_player = 'O' if current_player == 'X' else 'X'


# Запуск игры
play_game()