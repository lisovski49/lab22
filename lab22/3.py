def create_chessboard(n, m):
    chessboard = []
    for i in range(n):
        row = []
        for j in range(m):
            if (i + j) % 2 == 0:
                row.append(".")
            else:
                row.append("*")
        chessboard.append(row)
    return chessboard
while True:
    try:
        n = int(input("Введите количество строк: "))
        m = int(input("Введите количество столбцов: "))

        chessboard = create_chessboard(n, m)

        for row in chessboard:
            print(" ".join(row))

        break

    except ValueError:
        print("Ошибка: введите целое число")

print("Программа завершена")
