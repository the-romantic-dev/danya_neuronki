import json

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
        for x in range(width):
            # Получаем цвет пикселя
            r, g, b = img_rgb.getpixel((x, y))

            # Добавляем цвет в список
            color_list.append((r / 255.0, g / 255.0, b / 255.0))

    return color_list


def generate(_generator, folder, data_len):
    json_data = {}
    for i in range(data_len):
        shapes = _generator.generate_shapes()
        _generator.save_image(f'{folder}/{filename(i)}')
        y_data = []
        for j in range(len(list(ShapeType))):
            elem = 0
            for shape in shapes:
                val = shape.shape_params.shape_type.value
                if j == val:
                    elem += 1
            y_data.append(elem)
        json_data[filename(i)] = {
            "y": y_data,
            "x": image_to_data(f"{folder}/{filename(i)}")
        }

    with open(f'{folder}/data.json', 'w') as file:
        json.dump(json_data, file)


if __name__ == '__main__':
    generator = RandomShapeGenerator(num_shapes=2, image_width=img_shape[0], image_height=img_shape[0],
                                     min_shape_size=20,
                                     max_shape_size=50)
    generate(generator, teach_folder, train_len)
    generate(generator, test_folder, test_len)
