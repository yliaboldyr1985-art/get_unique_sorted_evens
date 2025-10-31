# get_unique_sorted_evens
  Возвращает список уникальных чётных чисел, отсортированных по убыванию
def get_unique_sorted_evens(numbers):
    """Возвращает список уникальных чётных чисел, отсортированных по убыванию."""
    # Убираем дубликаты с помощью set и фильтруем чётные числа
    evens = {n for n in numbers if n % 2 == 0}
    # Возвращаем отсортированный по убыванию список
    return sorted(evens, reverse=True)


if __name__ == "__main__":
    # Ввод данных пользователем
    user_input = input("Введите числа через пробел: ")
    # Преобразуем введённые данные в список целых чисел
    numbers = list(map(int, user_input.split()))
    # Вызываем функцию и выводим результат
    result = get_unique_sorted_evens(numbers)
    print("Результат:", result)
