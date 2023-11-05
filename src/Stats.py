import time

import pandas as pd

from src.Globals import Globals

from src.FileManager import load_data


class StatClass:
    def __init__(self, task_manager, gui):
        '''функция-конструктор для объекта класса,
        принимает менеджер заданиями для определения номера задания и gui для вывода туда задания,
        ничего не возращает'''
        self.task_manager = task_manager
        self.gui = gui
        self.typing = False
        self.errors = 0
        self.prev_errors = 0
        self.start_time = 0
        self.typing_speed = 0
        self.characters_typed = 0
        loaded_data = load_data()
        if loaded_data is not None:
            self.error_keys = loaded_data
        else:
            self.error_keys = pd.DataFrame({'Character': list(Globals.allowed_characters), 'Count': 0})

    def clear_stats(self):
        '''функция для очистки статистики в gui, ничего не принимает, ничего не возращает'''
        self.prev_errors = self.errors
        self.errors = 0
        self.start_time = 0
        if self.gui is not None:
            self.update_stats_label()

    def update_stats_label(self):
        '''функция для обновления статистики в онлайне, ничего не принимает, ничего не возвращает'''
        if self.typing:
            elapsed_time = time.time() - self.start_time
            if elapsed_time != 0:
                self.typing_speed = self.characters_typed / elapsed_time
            else:
                self.typing_speed = 0
            stats_text = f"Задание {self.task_manager.current_task_index + 1}\n"
            stats_text += f"Ошибки: {self.errors}, Скорость печати: {self.typing_speed:.2f} символов/сек"
            self.gui.stats_label.config(text=stats_text)
        else:
            self.gui.stats_label. \
                config(text=f"Задание {self.task_manager.current_task_index} Завершено. Ошибки: {self.prev_errors}")

    def clear_stat_history(self):
        '''функция для очистки истории статистики, ничего не принимает, ничего не возвращает'''
        with open('data/stat.txt', 'w'):
            pass
