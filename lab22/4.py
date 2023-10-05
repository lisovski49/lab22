try:
    x = int(input("Введите число: "))
    result = 10 / x
    print("Результат: ", result)

except ZeroDivisionError:
    print("Ошибка: деление на ноль")

except ValueError:
    print("Ошибка: введите целое число")

finally:
    print("Программа завершена")
