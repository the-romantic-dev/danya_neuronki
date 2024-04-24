import json

from config import img_shape, hidden_layer_size, activation, test_folder, test_len, filename
from data.enum_shape_type import ShapeType
from nn.ffnn import FFNN

if __name__ == '__main__':
    model = FFNN(
        hidden_layer_size=hidden_layer_size,
        shape=img_shape,
        activation=activation,
        total_shapes_num=len(list(ShapeType))
    )

    model.load()
    test_x = []
    test_y = []
    with open(f'{test_folder}/data.json', 'r') as file:
        data_json = json.load(file)

    for i in range(test_len):
        test_x.append(data_json[filename(i)]["x"])
        test_y.append(data_json[filename(i)]["y"])
    predicted_y = model.predict(test_x)
    for i in range(test_len):
        print(f"{test_y[i]} | {predicted_y[i]}")
