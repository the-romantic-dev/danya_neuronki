from dataclasses import dataclass

from data.class_color import Color
from data.data_class_shape_box import ShapeBox
from data.enum_shape_type import ShapeType
from data.enum_stretch_direction import StretchDirection


@dataclass
class ShapeParams:
    shape_box: ShapeBox
    color: Color
    shape_type: ShapeType
