import math
import random

from data.class_color import Color
from data.data_class_shape_box import ShapeBox
from data.data_class_shape_params import ShapeParams
from data.enum_shape_type import ShapeType


def shape_box_center(shape_box: ShapeBox) -> tuple:
    horizontal_center = (shape_box.left + shape_box.right) / 2
    vertical_center = (shape_box.bottom + shape_box.top) / 2
    return horizontal_center, vertical_center


def shape_box_radius(shape_box: ShapeBox) -> tuple:
    horizontal_radius = (shape_box.right - shape_box.left) / 2
    vertical_radius = (shape_box.top - shape_box.bottom) / 2
    return horizontal_radius, vertical_radius


class Shape:

    def __init__(self, shape_params: ShapeParams):
        self.shape_params = shape_params
        self.center_x, self.center_y = shape_box_center(shape_params.shape_box)
        self.radius_x, self.radius_y = shape_box_radius(shape_params.shape_box)
        self.points = self.__points()

    @staticmethod
    def random(shape_box: ShapeBox):
        color = Color.random()
        shape_params = ShapeParams(
            shape_box=shape_box, color=color, shape_type=random.choice(list(ShapeType))
        )
        return Shape(shape_params)

    def __points(self):
        shape_type = self.shape_params.shape_type
        points = []

        if shape_type == ShapeType.RECTANGLE:
            points = self.__rectangle_points()
        elif shape_type == ShapeType.ELLIPSE:
            points = self.__ellipse_points()
        elif shape_type == ShapeType.TRIANGLE:
            points = self.__triangle_points()
        elif shape_type == ShapeType.PENTAGON:
            points = self.__pentagon_points()
        elif shape_type == ShapeType.STAR:
            points = self.__star_points()

        return points

    def __rectangle_points(self):
        shape_box = self.shape_params.shape_box
        return [
            (shape_box.left, shape_box.bottom),
            (shape_box.right, shape_box.bottom),
            (shape_box.right, shape_box.top),
            (shape_box.left, shape_box.top)
        ]

    def __polygon_points(self, sides: int):
        result = []
        angle_increment = 2 * math.pi / sides
        for i in range(sides):
            angle_rad = i * angle_increment
            x = self.center_x + self.radius_x * math.cos(angle_rad)
            y = self.center_y + self.radius_y * math.sin(angle_rad)
            result.append((x, y))
        return result

    def __ellipse_points(self):
        return self.__polygon_points(sides=36)

    def __triangle_points(self):
        shape_box = self.shape_params.shape_box
        return [
            (shape_box.left, shape_box.bottom),
            (shape_box.right, shape_box.bottom),
            (self.center_x, shape_box.top)
        ]

    def __pentagon_points(self):
        return self.__polygon_points(sides=5)

    def __star_points(self):
        result = []
        sides = 5
        angle_increment = 2 * math.pi / sides
        radius_inner_x = self.radius_x / 2.5
        radius_inner_y = self.radius_y / 2.5
        for i in range(sides):
            angle_rad = i * angle_increment
            outer_x = self.center_x + self.radius_x * math.cos(angle_rad)
            outer_y = self.center_y + self.radius_y * math.sin(angle_rad)
            result.append((outer_x, outer_y))
            inner_angle_rad = angle_rad + angle_increment / 2
            inner_x = self.center_x + radius_inner_x * math.cos(inner_angle_rad)
            inner_y = self.center_y + radius_inner_y * math.sin(inner_angle_rad)
            result.append((inner_x, inner_y))
        return result
