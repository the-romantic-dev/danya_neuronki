import json
from copy import deepcopy
from pathlib import Path

import numpy as np
from keras import Sequential
from keras.src.callbacks import History
from keras.src.layers import Dense, Flatten, Dropout


class FFNN:
    def __init__(
            self, hidden_layer_num: int, hidden_layer_size: int, output_layer_size: int, shape: tuple[int, int],
            hidden_layer_activation: str, output_layer_activation: str, fit_data_folder: str):

        self.hidden_layer_num = hidden_layer_num
        self.fit_data_folder = fit_data_folder

        model = Sequential()
        # Инициализируем слои
        # Количество входных нейронов равно количеству пикселей. Каждый нейрон принимает 3 признака (RGB)
        model.add(
            Dense(units=hidden_layer_size, activation=hidden_layer_activation, input_shape=(shape[0], shape[1], 3))
        )

        # Добавляем заданное количество скрытых слоев
        for i in range(1, hidden_layer_num):
            model.add(Dense(units=hidden_layer_size, activation=hidden_layer_activation))
            model.add(Dropout(0.25))
        # Flatten преобразует выход скрытых слоев в одномерный вектор
        model.add(Flatten())
        model.add(Dense(units=output_layer_size, activation=output_layer_activation))
        # Компилируем модель
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        print(model.summary())

        self.model = model
        self.fit_data: History = None

    def fit(self, train_x: list[list[list[float, float, float]]], train_y: list[list[float]], epochs: int):
        self.fit_data = self.model.fit(np.array(train_x), np.array(train_y), epochs=epochs, validation_split=0.4)

    def predict(self, predictable_data: list[list[tuple[float, float, float]]]):
        return self.model.predict(np.array(predictable_data))

    def save(self):
        filename = "model.weights.h5"
        self.model.save_weights(filename)
        json_data = deepcopy(self.fit_data.history)
        json_data['epoch'] = self.fit_data.epoch
        json_path = Path.cwd()
        with open(f'{self.fit_data_folder}/plot_data_for_{self.hidden_layer_num}_layers.json', 'w') as file:
            json.dump(json_data, file)

    def load(self):
        filename = "model.weights.h5"
        self.model.load_weights(filename)
