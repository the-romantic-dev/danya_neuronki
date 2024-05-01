import json
from itertools import combinations

from PIL import Image

from config import train_len, teach_folder, img_shape, filename, test_folder, test_len
from data.class_random_shapes_generator import RandomShapeGenerator
import shutil

from data.enum_shape_type import ShapeType


def image_to_data(image_path: str):
    # Открываем изображение
    img = Image.open(image_path)

    # Получаем размеры изображения
    width, height = img.size

    # Преобразуем изображение в режим RGB
    img_rgb = img.convert("RGB")

    # Создаем пустой список для хранения цветов пикселей
    color_list = []

    # Проходимся по каждому пикселю изображения
    for y in range(height):
        row = []
        for x in range(width):
            # Получаем цвет пикселя
            r, g, b = img_rgb.getpixel((x, y))

            # Добавляем цвет в список
            row.append((r / 255.0, g / 255.0, b / 255.0))
            # if r == 0 and g == 0 and b == 0:
            #     color_list.append(1)
            # else:
            #     color_list.append(0)
        color_list.append(row)
    return color_list


def generate(_generator, folder, data_len, encoding_dict: dict):
    json_data = {}
    for i in range(data_len):
        shapes = _generator.generate_shapes()
        _generator.save_image(f'{folder}/{filename(i)}')
        key = frozenset([s.shape_params.shape_type for s in shapes])
        y_data = encoding_dict[key]
        json_data[filename(i)] = {
            "y": y_data,
            "x": image_to_data(f"{folder}/{filename(i)}")
        }

    with open(f'{folder}/data.json', 'w') as file:
        json.dump(json_data, file)


def generate_combinations_to_encoding(k: int):
    shape_types = list(ShapeType)
    class_combinations = []
    class_combinations.extend(combinations(shape_types, k))

    encoded_combinations = []
    for i, combo in enumerate(class_combinations):
        encoded_combo = []
        for j, _ in enumerate(class_combinations):
            if j == i:
                encoded_combo.append(1)
            else:
                encoded_combo.append(0)
        encoded_combinations.append(encoded_combo)

    result = {}
    for i in range(len(class_combinations)):
        result[frozenset(class_combinations[i])] = encoded_combinations[i]
    return result


if __name__ == '__main__':
    num_shapes = 2
    generator = RandomShapeGenerator(num_shapes=num_shapes, image_width=img_shape[0], image_height=img_shape[0],
                                     min_shape_size=20,
                                     max_shape_size=100)
    combinations_to_encoding = generate_combinations_to_encoding(num_shapes)
    generate(generator, teach_folder, train_len, combinations_to_encoding)
    generate(generator, test_folder, test_len, combinations_to_encoding)
