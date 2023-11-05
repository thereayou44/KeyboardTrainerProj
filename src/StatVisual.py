import plotly.graph_objects as go
from matplotlib import image as mpimg, pyplot as plt
import pylab


def show_stats():
    '''функция построения графиков скорости печати, ничего не принимает, ничего не возвращает'''
    with open('data/stat.txt', 'r') as file:
        lines = file.readlines()

    if lines:
        launches = []
        speeds = []

        for line in lines:
            parts = line.split()
            if len(parts) == 2:
                launches.append(int(parts[0]))
                speeds.append(float(parts[1]))

        if launches and speeds:
            fig, ax = pylab.subplots(figsize=(10, 6))
            x_values = range(1, len(launches) + 1)
            ax.plot(x_values, speeds, marker='o')
            ax.set_xlabel('Номер запуска программы')
            ax.set_ylabel('Символов в секунду')
            ax.set_title('График для скорости печати')
            ax.grid(True)
            ax.set_xticks(range(1, len(launches) + 1))
            pylab.tight_layout()
            pylab.show()


class StatVisualization:
    def __init__(self, stat_class):
        '''функция-конструктор класса StatVisualization,
         принимает класс статистики для которого нужна визулизация,
         ничего не возвращает'''

        self.stat_class = stat_class

    def create_key_heatmap(self):
        '''функция построения heatmap, ничего не принимает, ничего не возвращает'''
        size = 15
        original_count_data = self.stat_class.error_keys['Count'].tolist()
        original_character_data = self.stat_class.error_keys['Character'].tolist()
        original_character_data[0] = 'Space'

        z_data = [original_count_data[i:i + size] for i in range(0, len(original_count_data), size)]
        text_data = [original_character_data[i:i + size] for i in range(0, len(original_character_data), size)]

        # Заполняем последний подсписок нулями, чтобы сделать его одинаковой длины с другими
        last_sublist = z_data[-1]
        last_sublist.extend([0] * (size - len(last_sublist)))

        fig = go.Figure(data=go.Heatmap(z=z_data, text=text_data,
                                        texttemplate="%{text}",
                                        textfont={"size": 18})
                        )
        fig.write_image("data/heatmap.png", format='png', width=1000, height=800)

        img = mpimg.imread("data/heatmap.png")

        plt.figure(figsize=(10, 8), dpi=100)
        plt.imshow(img)
        plt.axis('off')
        plt.show()


