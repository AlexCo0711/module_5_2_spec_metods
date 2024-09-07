# Домашняя работа по уроку "Специальные методы классов"

# Для решения этой задачи используется решение к
# предыдущей задаче "Атрибуты и методы объекта".(module_5_1.py)

# Объявление класса House
class House():
    # инициализация характеристик класса House - имя и этажность
    def __init__(self, name, number_of_floors):
        # присвоение self.name значения name (имя здания)
        self.name = name
        # присвоение self.number_of_floors значения number_of_floors (этажность здания)
        self.number_of_floors = number_of_floors

    # реализация метода __len__ для возвращения количества этажей здания
    def __len__(self):
        # возвращаем значение количества этажей определенных в методе __init__
        return self.number_of_floors

    # реализация метода __str__ для возвращения строки "Название: <название>,
    # кол-во этажей: <этажи>".
    def __str__(self):
        # возвращаем f строку (форматированная строка, значения в {}
        # принимают ранее присвоенные значения из метода __init__)
        return (f"Название: {self.name}, кол-во этажей: {self.number_of_floors}")

    # Создание метода go_to с параметром new_floor и
    # логикой внутри него на основе описания задачи
    # и атрибутом new_floor для "плюшек"
    def go_to(self, new_floor):
        self.new_floor = new_floor
        # Если new_floor больше чем self.number_of_floors или меньше 1,
        # то вывод строки "Такого этажа не существует"
        if int(new_floor) > int(self.number_of_floors) or 1 > int(new_floor):
            print(f'Такого этажа {self.new_floor} не существует в доме "{self.name}"\nВ доме "{self.name}" не более {self.number_of_floors} этажей')
        # вывод на экран (в консоль) значения от 1 до new_floor(включительно)
        else:
            print(f'Этажи в доме "{self.name}":')
            for i in range(int(new_floor)):
                i += 1
                print(i)

# Исходные данные задачи
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
