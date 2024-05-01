from math import comb

from data.enum_shape_type import ShapeType
from nn.ffnn import FFNN

train_len = 100
test_len = 50
img_shape = (100, 100)
teach_folder = "teach_data"
test_folder = "test_data"
fit_data_folder = "plot_data"
filename = lambda i: f"shapes_{i}.png"
hidden_layer_num = 5
hidden_layer_size = 3
epochs = 50
hidden_layer_activation = "relu"
output_layer_activation = "softmax"

nn_model = FFNN(
    hidden_layer_num=hidden_layer_num,
    hidden_layer_size=hidden_layer_size,
    output_layer_size=comb(len(list(ShapeType)), 2),
    shape=img_shape,
    hidden_layer_activation=hidden_layer_activation,
    output_layer_activation=output_layer_activation,
    fit_data_folder=fit_data_folder
)
