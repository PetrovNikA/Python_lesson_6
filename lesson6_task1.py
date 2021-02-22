# Задача 1.
# Создать класс TrafficLight(светофор).
# определить у него один атрибут color(цвет) и метод running(запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния(красный) составляет 7 секунд, второго(жёлтый) — 2 секунды,
# третьего(зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке(красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep
from itertools import cycle


class TrafficLight:

    def __init__(self):
        self.__color = (('Red', 7), ('Yellow', 2), ('Green', 3))

    def running(self):
        for color, sec in cycle(self.__color):
            print(color, '(wait {} sec)'.format(sec))
            sleep(sec)


traffic_light = TrafficLight()
traffic_light.running()
