package main

import "fmt"
import "encoding/json"

func fibr(n int) int {
	// Генератор чисел Фибоначчи
	// Источник: http://progopedia.ru/example/fibonacci/204/
	if n < 2 {
		return 1
	}
	result := fibr(n-2) + fibr(n-1)

	return result
}

func userInput() int {
	// Функция ввода с консоли
	fmt.Print("Введите число ('Начинать с 1'): ")

	var input int
	fmt.Scanf("%d", &input)
	output := input

	return output
}

func main() {
	fibPosition := 0   // текущий порядковый номер числа Фибоначчи
	attemps := 10      // количество правильных ответов, которые необходимо пройти
	countAttemps := 0  // количество данных правильных ответов
	mistakes := 3      // количество допустимых ошибок
	countMistakes := 0 // количество допущенных ошибок

	for countAttemps <= attemps { // цикл по перебору чисел Фибоначчи
		if countMistakes < mistakes {
			data := userInput()
			fib := fibr(fibPosition)
			fmt.Println("current fibnumber: ", fib)
			fmt.Println("current attemps / mistakes: ", countAttemps, "/", countMistakes)
			if data == fib {
				fmt.Println("Молодец, правильный ответ: ", fib)
				countAttemps = countAttemps + 1
			} else {
				err := map[int]int{ // Карта ошибки
					fib: fibPosition,
				}
				mapJSON, _ := json.Marshal(err) // Преобразуем в JSON
				fmt.Print("Вы ошиблись, правильный ответ: ")
				fmt.Println(string(mapJSON)) // Выводим предупреждение и пару в JSON

				countMistakes = countMistakes + 1 // Увеличиваем кол-во ошибок
				countAttemps = 0                  // Обнуляем кол-во правильных ответов
			}
		} else {
			fmt.Println("Совершено более трех ошибок")
			break
		}
		fibPosition = fibPosition + 1 // Увеличиваем порядковый номер числа Фибоначчи
	}
}

// 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040

// Если пользователь допустил ошибку или не ввел число в течении 10ти секунд,
// программа сама выводит текущее число и его порядковый номер (в виде json объекта) на экран и
// пользователь продолжает последовательность со следующего.
