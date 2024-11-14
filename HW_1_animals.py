class Animal:
    def __init__(self, name, sound):
        self.name = name  # Имя животного
        self.sound = sound  # Звук, который оно издает

    def makesound(self):
        print(f"{self.name} говорит: {self.sound}")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Мяу")  
        self.color = color  # Цвет кота

    def makesound(self):
        print(f"{self.name} ({self.color}) говорит: Мяу")


class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Гав")  
        self.color = color

    def makesound(self):
        print(f"{self.name} ({self.color}) говорит: Гав")


cat = Cat(name="Барсик", color="Белый")
dog = Dog(name="Шарик", color="Коричневый")


cat.makesound()  
dog.makesound()  
