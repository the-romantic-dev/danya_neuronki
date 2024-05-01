import json

import numpy as np

from config import nn_model, test_folder, test_len, filename

if __name__ == '__main__':
    nn_model.load()

    test_x = []
    test_y = []
    with open(f'{test_folder}/data.json', 'r') as file:
        data_json = json.load(file)

    for i in range(test_len):
        test_x.append(data_json[filename(i)]["x"])
        test_y.append(data_json[filename(i)]["y"])
    predicted_y = list(nn_model.predict(test_x))
    total_equals = 0
    for i in range(test_len):
        current_predicted = list(predicted_y[i])
        current_expected = list(test_y[i])
        max_elem_index = current_predicted.index(max(current_predicted))
        discrete_predicted_y = []
        for j in range(len(current_predicted)):
            if j == max_elem_index:
                discrete_predicted_y.append(1)
            else:
                discrete_predicted_y.append(0)

        print(f"{current_expected} | {discrete_predicted_y} | {current_predicted}")
        if test_y[i] == discrete_predicted_y:
            total_equals += 1

    print(f"Всего совпадений {total_equals} / {test_len}")
