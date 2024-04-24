import json

from PIL import Image

from config import img_shape, train_len, teach_folder, filename, activation, hidden_layer_size
from data.enum_shape_type import ShapeType
from nn.ffnn import FFNN





if __name__ == '__main__':
    model = FFNN(
        hidden_layer_size=hidden_layer_size,
        shape=img_shape,
        activation=activation,
        total_shapes_num=len(list(ShapeType))
    )
    train_x = []
    train_y = []
    with open(f'{teach_folder}/data.json', 'r') as file:
        data_json = json.load(file)

    for i in range(train_len):
        train_x.append(data_json[filename(i)]["x"])
        train_y.append(data_json[filename(i)]["y"])

    model.fit(train_x, train_y, epochs=30)
    model.save()
