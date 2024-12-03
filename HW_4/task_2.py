"""
Изучите модуль itertools в Python. Напишите программу, которая использует этот модуль 
для решения следующих задач:
- Создание бесконечного генератора чисел.
- Применение функций к каждому элементу в итераторе.
- Объединение нескольких итераторов в один.
- Используйте функции и методы из модуля itertools, чтобы выполнить указанные задачи. 
- Убедитесь, что ваш скрипт может обрабатывать исключения, связанные с отсутствием данных 
в итераторах.
"""

import itertools


def besk():
    """Создает бесконечный генератор чисел"""
    for number in itertools.count(start=1, step=1):
        yield number


def apply_func(iterator, func):
    """Применяет функцию к каждому элементу в итераторе"""
    for item in iterator:
        try:
            result = func(item)
            print(f"Применение функции к {item}: {result}")
        except Exception as e:
            print(f"Ошибка при обработке элемента {item}: {e}")


def combine(*iterators):
    """Объединяет несколько итераторов в один"""
    try:
        combined_iterator = itertools.chain(*iterators)
        for item in combined_iterator:
            print(f"Объединенный элемент: {item}")
    except Exception as e:
        print(f"Ошибка при объединении итераторов: {e}")


# Пример использования бесконечного генератора чисел
print("Бесконечный генератор чисел:")
generator = besk()
for _ in range(10):
    print(next(generator))

# Пример применения функции к каждому элементу в итераторе
print("\nПрименение функции к каждому элементу в итераторе:")
iterator = [1, 2, 3, "a", 5]
apply_func(iterator, lambda x: x * 2)

# Пример объединения нескольких итераторов
print("\nОбъединение нескольких итераторов:")
iter1 = [1, 2, 3]
iter2 = ["a", "b", "c"]
iter3 = [4, 5, 6]
combine(iter1, iter2, iter3)
# Пример обработки исключения при объединении итераторов
print("\n исключения при объединении:")
combine(iter1, None, iter3)
