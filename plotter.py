import json
import os.path

from matplotlib import pyplot as plt

from config import fit_data_folder


def show_history_plot(_plot_data: dict[int, dict], name: str):
    for layers_num in _plot_data:
        pd = _plot_data[layers_num]
        add_plot(pd['epoch'], pd[name], name=f"{name} при {layers_num} слоях")
    plt.legend()
    plt.xlabel('Эпохи')
    plt.ylabel(f'Значение {name}')
    plt.show()

def add_plot(x, y, name: str):
    plt.plot(x, y, label=name)

if __name__ == '__main__':
    max_layers_num = 5
    plot_data = {}
    for i in range(max_layers_num):
        filepath = f'{fit_data_folder}/plot_data_for_{i + 1}_layers.json'
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                plot_data[i + 1] = json.load(file)
    show_history_plot(_plot_data=plot_data, name='accuracy')
    show_history_plot(_plot_data=plot_data, name='loss')
    show_history_plot(_plot_data=plot_data, name='val_accuracy')
    show_history_plot(_plot_data=plot_data, name='val_loss')
