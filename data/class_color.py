import random


class Color:
    def __init__(self, r: int, g: int, b: int):
        self.__rgb = (r, g, b)

    def rgb(self):
        return self.__rgb

    @staticmethod
    def random():
        return Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
