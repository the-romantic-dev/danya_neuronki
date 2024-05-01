import json

from config import nn_model, train_len, teach_folder, filename, epochs

if __name__ == '__main__':
    train_x = []
    train_y = []
    with open(f'{teach_folder}/data.json', 'r') as file:
        data_json = json.load(file)

    for i in range(train_len):
        train_x.append(data_json[filename(i)]["x"])
        train_y.append(data_json[filename(i)]["y"])

    nn_model.fit(train_x, train_y, epochs=epochs)

    nn_model.save()
