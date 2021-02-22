# Задача 5.
# Реализовать класс Stationery(канцелярская принадлежность).
# определить в нём атрибут title(название) и метод draw(отрисовка).Метод выводит сообщение «Запуск отрисовки»;
# cоздать три дочерних класса Pen(ручка), Pencil(карандаш), Handle(маркер);
# в каждом классе реализовать переопределение метода draw.Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


# Родитель
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

# Потомки
class Pen(Stationery):
    def draw(self):
        print('Ручка рисует')


class Pencil(Stationery):
    def draw(self):
        print('Карандаш рисует')


class Handle(Stationery):
    def draw(self):
        print('Маркер рисует')

# Создание объектов
pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')

# Применение методов к объектам
pen.draw()
pencil.draw()
handle.draw()
