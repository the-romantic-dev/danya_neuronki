import random
from PIL import Image, ImageDraw
from data.class_color import Color
from data.class_shape import Shape
from data.data_class_shape_box import ShapeBox
from data.enum_shape_type import ShapeType
from data.util import is_shape_box_overlapping, is_shape_box_included


class RandomShapeGenerator:
    def __init__(self, num_shapes, image_width, image_height, min_shape_size, max_shape_size):
        self.num_shapes = num_shapes
        self.image_width = image_width
        self.image_height = image_height
        self.min_shape_size = min_shape_size
        self.max_shape_size = min(max_shape_size, image_width // 2, image_height // 2)
        bg_color = Color.random().rgb()
        self.image = Image.new('RGB', (image_width, image_height), color=bg_color)
        self.draw = ImageDraw.Draw(self.image)
        self.shapes = []

    def generate_shapes(self) -> list[Shape]:
        if len(self.shapes) > 0:
            self.clear()
        for _ in range(self.num_shapes):
            shape_box = self.generate_shape_box()
            shape = Shape.random(shape_box, self.is_double_type)
            self.draw_shape(shape)
            self.shapes.append(shape)
        return self.shapes

    def is_double_type(self, shape_type: ShapeType) -> bool:
        for ex_shape in self.shapes:
            if shape_type == ex_shape.shape_params.shape_type:
                return True
        return False

    def generate_shape_box(self):
        # Генерация закончится как только будет ShapeBox не пересекающийся с уже созданными ShapeBox.
        while True:
            size_x = random.randint(self.min_shape_size, self.max_shape_size)
            size_y = random.randint(self.min_shape_size, self.max_shape_size)
            x1 = random.randint(size_x, self.image_width - size_x + 1)
            y1 = random.randint(size_y, self.image_height - size_y + 1)
            x2 = x1 + size_x
            y2 = y1 + size_y
            shape_box = ShapeBox(left=x1, bottom=y1, right=x2, top=y2)

            if self.is_shape_overlapping(shape_box) or self.is_shape_out_of_bounds(shape_box):
                continue
            return shape_box

    def is_shape_overlapping(self, shape_box: ShapeBox):
        for existing_shape in self.shapes:
            existing_shape_box = existing_shape.shape_params.shape_box
            if is_shape_box_overlapping(shape_box, existing_shape_box):
                return True
        return False

    def is_shape_out_of_bounds(self, shape_box: ShapeBox):
        image_shape_box = ShapeBox(left=0, bottom=0, right=self.image_width, top=self.image_height)
        return not is_shape_box_included(parent_box=image_shape_box, child_box=shape_box)

    def draw_shape(self, shape: Shape):
        self.draw.polygon(shape.points, fill=shape.shape_params.color.rgb())

    def save_image(self, filename):
        self.image.save(filename)

    def clear(self):
        bg_color = Color.random().rgb()
        # bg_color = Color(255, 255, 255).rgb()
        self.image = Image.new('RGB', (self.image_width, self.image_height), color=bg_color)
        self.draw = ImageDraw.Draw(self.image)
        self.shapes = []
