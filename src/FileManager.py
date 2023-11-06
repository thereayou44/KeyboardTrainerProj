from tkinter import filedialog

import pandas as pd


def load_data():
    '''Функция для загрузки сведений об ошибках из файла, чтобы не терять их при следующем запуске,
     ничего не принимает, ничего не возвращает'''
    try:
        return pd.read_csv('data/error_keys_data.csv')
    except FileNotFoundError:
        return


def save_data(error_keys):
    '''Сохранение сведений об ошибках'''
    error_keys.to_csv('data/error_keys_data.csv', index=False)


class FileManager:
    def __init__(self, task_class):
        '''функция-конструктор для менеджера файлами, принимает объект менеджера задач, ничего не возращает '''
        self.task_class = task_class
        self.is_new_launch = True
        self.speed_sum = 0

    def load_tasks_from_file(self):
        '''Загрузка задач из файла, ничего не принимает, ничего не возвращает'''
        self.task_class.current_task_index = 0
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.gna")])
        if file_path:
            self.task_class.tasks = []
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()
                tasks = file_content.split('---')
                for task in tasks:
                    cleaned_task = task.strip().replace('\n', ' ').strip()
                    if cleaned_task:
                        self.task_class.tasks.append(cleaned_task)

        self.task_class.load_task()

    def save_stats_to_file(self, is_end, typing_speed):
        '''Функия для записи скорости в файл после завершения всех задач,
         принимает флаг закончились ли задания и скорость печати для каждого задания, ничего не возращает'''
        if is_end:
            with open('data/stat.txt', 'a+') as file:
                file.seek(0)
                lines = file.readlines()
                if lines:
                    if self.is_new_launch:
                        current_launch = int(lines[-1].split(' ')[0]) + 1
                        self.is_new_launch = False
                else:
                    self.is_new_launch = False
                if len(self.task_class.tasks):
                    line = f"{current_launch} {self.speed_sum / len(self.task_class.tasks):.2f}\n"
                file.seek(0, 2)
                file.write(line)
        else:
            self.speed_sum += typing_speed
