from data.data_class_shape_box import ShapeBox


def is_shape_box_overlapping(box_1: ShapeBox, box_2: ShapeBox):
    max_left = max(box_1.left, box_2.left)
    max_bottom = max(box_1.bottom, box_2.bottom)
    min_right = min(box_1.right, box_2.right)
    min_top = min(box_1.top, box_2.top)
    if max_left < min_right or max_bottom > min_top:
        return True
    return False


def is_shape_box_included(parent_box: ShapeBox, child_box: ShapeBox):
    is_horizontal_inside = parent_box.left <= child_box.left <= child_box.right <= parent_box.right
    is_vertical_inside = parent_box.bottom <= child_box.bottom <= child_box.top <= parent_box.top
    return is_horizontal_inside and is_vertical_inside



