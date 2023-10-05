def nod(a, b):

    while b:
        a, b = b, a % b
    return a

def nok(a, b):

    try:
        return (a * b) // nod(a, b)
    except ZeroDivisionError:
        print("Ошибка: одно из чисел равно нулю")
        return None
    finally:
        print("Выполнение функции nok завершено")

# Пример использования функции lcm
while True:
    try:
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
        break
    except ValueError:
        print("Ошибка: введите целое число")

result = nok(num1, num2)
if result is not None:
    print("Наименьшее общее кратное:", result)
