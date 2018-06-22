import sys, select
import json


# Глобальные переменные:
attemps = 10            # количество правильных ответов, которые необходимо пройти
mistakes = 0            # количество допускаемых ошибок
count_attempts = 0      # количество данных правильных ответов
count_mistakes = 3      # количество допущенных ошибок
current_index = 0       # порядковый номер числа Фибоначчи
start = "первое число (начиная с 0)" # вариация стартового сообщения о вводе числа Фибоначчи


def fibonacci():
    """Генератор ряда чисел Фибоначчи"""
    a, b = 0, 1
    while True:
        yield a            # return a, + запоминаем место рестарта для следующего вызова
        a, b = b, a + b


fibonacci_generator = fibonacci()                                           # запускаем генератор

while count_attempts < attemps and count_mistakes > mistakes:               # цикл для обработки вводимых чисел

    fib = next(fibonacci_generator)                                         # вызываем первое или очередное число
    current_index += 1

    timeout = 10                                                            # время ожидания ввода данных пользователем
    print(f"\nУкажите {start} из ряда Фибоначчи: ")

    input_number, o, e = select.select([sys.stdin], [], [], timeout)        # последний параметр - seconds

    if input_number:                                                        # если пользователь что-то ввёл
        try:
            input_data = int(sys.stdin.readline().strip())
            print("Вы ввели: ", input_data)                                 # delete row
        except (ValueError, NameError):
            print("Ошибка! Вам следует ввести целое число")


        if input_data == fib:
            print(f"Текущее число Фибоначчи: {fib}")                                     # delete row
            print(f"Порядковый номер числа: {current_index}")                            # delete row
            count_attempts += 1
            start = f" число № {current_index}"
            print(
                f"Вы правильно указали число {input_data} из ряда Фибоначчи.\n"
                f"Вам нужно указать еще {attemps - count_attempts} чисел (числа)")
        else:
            print(f"Текущее число Фибоначчи: {fib}")                                     # delete row
            print(f"Порядковый номер числа: {current_index}")                            # delete row
            mistakes_out = {fib : current_index}
            mistakes_out = json.JSONEncoder().encode(mistakes_out)
            count_attempts = 0
            count_mistakes -= 1
            start = f" число № {current_index}"
            print(f"Вы ошиблись! Текущее число и его порядковый номер {mistakes_out}. \n"
                  f"У Вас осталось {count_mistakes} попытка (попытки)")
    else:
        mistakes_out = {fib: current_index}
        mistakes_out = json.JSONEncoder().encode(mistakes_out)
        count_attempts = 0
        count_mistakes -= 1
        current_index += 1
        start = f" число № {current_index}"
        print(f"Вы задержались с ответом! Текущее число Фибоначчи и его порядковый номер {mistakes_out}. \n"
              f"У Вас осталось {count_mistakes} попытка (попытки)")


# Если пользователь допустил ошибку или не ввел число в течении 10ти секунд,
# программа сама выводит текущее число и его порядковый номер (в виде json объекта) на экран и
# пользователь продолжает последовательность со следующего.
