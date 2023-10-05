import string
import math

def process_input(input_data):
    try:
        if isinstance(input_data, list):
            unique_elements = set(input_data)
            print("Уникальные элементы списка:", unique_elements)
            geometric_mean = math.prod(unique_elements) ** (1/len(unique_elements))
            print("Среднее геометрическое всех чисел:", geometric_mean)
        elif isinstance(input_data, dict):
            keys_list = list(input_data.keys())
            print("Ключи словаря:", keys_list)
        elif isinstance(input_data, int):
            num_digits = len(str(abs(input_data)))
            print("Количество разрядов числа:", num_digits)
        elif isinstance(input_data, str):
            if any(char in string.punctuation for char in input_data):
                print("Строка содержит знаки препинания")
            else:
                words = input_data.split()
                palindrome_count = 0
                for word in words:
                    if word == word[::-1]:
                        palindrome_count += 1
                print("Количество палиндромов в строке:", palindrome_count)
        else:
            print("Неподдерживаемый тип данных")
    except Exception as e:
        print("Ошибка:", e)
    finally:
        print("Обработка входных данных завершена")

while True:
    input_data = input("Введите данные: ")

    try:
        input_data = eval(input_data)
    except:
        pass

    process_input(input_data)