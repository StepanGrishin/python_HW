"""
Создайте пакет, где будет находиться модуль, который содержит класс с методом, 
вычисляющий сумму всех чисел в передаваемом списке. В качестве решения сдать сам 
пакет и обращение к нему.
"""

from my_package.my_module import NumberSum

# Создаем экземпляр класса
number_sum = NumberSum()

# Передаем список чисел и вычисляем сумму
numbers_list = [23, 56, 1, 4, 5]
result = number_sum.sum_numbers(numbers_list)

print(f"Сумма чисел в списке: {result}")
