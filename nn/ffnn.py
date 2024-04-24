import numpy as np
from keras import Input, Model
from keras.src.layers import Dense, Flatten, Dropout


class FFNN:
    def __init__(self, hidden_layer_size: int, shape: tuple[int, int], activation: str, total_shapes_num: int):
        # Инициализируем слои
        # Количество входных нейронов равно количеству пикселей. Каждый нейрон принимает 3 признака (RGB)
        input_layer = Input(shape=(shape[0] * shape[1], 3), name="Input")
        # Скрытый слой размера hidden_layer_size c функцией активации activation
        hidden_layer = Dense(units=hidden_layer_size, activation=activation, name="Hidden")(input_layer)
        # Скрытый слой имеет выход размерности (hidden_layer_size, 3).
        # Flatten преобразует выход слоя (hidden_layer_size, 3) в (hidden_layer_size * 3, 1)
        flattened_layer = Flatten()(hidden_layer)
        # Выходной слой получает выход flattened_layer
        output_layer = Dense(units=total_shapes_num, name="Output", activation="sigmoid")(flattened_layer)
        # На выходе всей модели имеем total_shapes_num чисел,
        # где каждый выход обозначает количество фигур данного типа
        model = Model(inputs=input_layer, outputs=output_layer)

        # Компилируем модель
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

        self.model = model

    def fit(self, train_x: list[list[list[float, float, float]]], train_y: list[list[float]], epochs: int):
        self.model.fit(np.array(train_x), np.array(train_y), epochs=epochs, validation_split=0.2)

    def predict(self, predictable_data: list[list[tuple[float, float, float]]]):
        return self.model.predict(np.array(predictable_data))

    def save(self):
        filename = "model.weights.h5"
        self.model.save_weights(filename)

    def load(self):
        filename = "model.weights.h5"
        self.model.load_weights(filename)
