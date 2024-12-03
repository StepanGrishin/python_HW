import datetime

# Класс для товара
class Product:
    def __init__(self, name, quantity, price):
        self.name = name  # Название товара
        self.quantity = quantity  # Количество на складе
        self.price = price  # Цена товара
    
    def increase_quantity(self, amount):
        """Увеличение количества товара."""
        self.quantity += amount
        print(f"Количество товара '{self.name}' увеличено на {amount}. Текущее количество: {self.quantity}.")
    
    def decrease_quantity(self, amount):
        """Уменьшение количества товара."""
        if self.quantity >= amount:
            self.quantity -= amount
            print(f"Количество товара '{self.name}' уменьшено на {amount}. Текущее количество: {self.quantity}.")
        else:
            print(f"Недостаточно товара '{self.name}' на складе. Доступно: {self.quantity}.")
    
    def calculate_value(self):
        """Расчёт стоимости товара на складе."""
        return self.quantity * self.price

# Класс для склада
class Warehouse:
    def __init__(self):
        self.products = []  # Список товаров на складе
    
    def add_product(self, product):
        """Добавление товара на склад."""
        self.products.append(product)
        print(f"Товар '{product.name}' добавлен на склад.")
    
    def remove_product(self, product_name):
        """Удаление товара со склада по имени."""
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f"Товар '{product_name}' удалён со склада.")
                return
        print(f"Товар '{product_name}' не найден на складе.")
    
    def total_value(self):
        """Расчёт общей стоимости всех товаров на складе."""
        total = sum(product.calculate_value() for product in self.products)
        return total
    
    def get_product(self, product_name):
        """Получение товара по имени."""
        for product in self.products:
            if product.name == product_name:
                return product
        return None

# Класс для продавца
class Seller:
    def __init__(self, name):
        self.name = name  # Имя продавца
        self.sales_log = []  # Лог продаж
    
    def sell_product(self, warehouse, product_name, quantity):
        """Продажа товара: уменьшение количества и расчёт выручки."""
        product = warehouse.get_product(product_name)
        if product:
            if product.quantity >= quantity:
                product.decrease_quantity(quantity)
                sale_value = quantity * product.price
                self.sales_log.append({
                    'product': product_name,
                    'quantity': quantity,
                    'total_value': sale_value,
                    'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
                print(f"Продано {quantity} единиц товара '{product_name}' на сумму {sale_value}.")
            else:
                print(f"Недостаточно товара '{product_name}' для продажи.")
        else:
            print(f"Товар '{product_name}' не найден на складе.")
    
    def sales_report(self):
        """Отчёт о продажах."""
        if self.sales_log:
            print(f"Отчёт о продажах продавца {self.name}:")
            for sale in self.sales_log:
                print(f"{sale['date']} | Товар: {sale['product']} | Количество: {sale['quantity']} | Стоимость: {sale['total_value']}")
        else:
            print(f"Отчётов о продажах нет.")

# Класс для ведения логирования операций
class Logger:
    @staticmethod
    def log(message):
        """Логирование действий."""
        with open("warehouse_log.txt", "a") as file:
            file.write(f"{datetime.datetime.now()} - {message}\n")
        print(f"Лог: {message}")

# Пример использования программы

# Создание склада
warehouse = Warehouse()

# Создание товаров
product1 = Product(name="Ноутбук", quantity=10, price=50000)
product2 = Product(name="Телефон", quantity=20, price=30000)

# Добавление товаров на склад
warehouse.add_product(product1)
warehouse.add_product(product2)

# Логирование операций
Logger.log("Товары добавлены на склад.")

# Создание продавца
seller = Seller(name="Иван")

# Продавец продает товары
seller.sell_product(warehouse, "Ноутбук", 2)
seller.sell_product(warehouse, "Телефон", 5)

# Логирование операций
Logger.log("Товары проданы.")

# Вывод отчета о продажах
seller.sales_report()

# Расчёт общей стоимости товаров на складе
print(f"Общая стоимость товаров на складе: {warehouse.total_value()}")

# Логирование операций
Logger.log("Запрашиваем общую стоимость товаров.")
