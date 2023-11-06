from src.Globals import Globals
import tkinter as tk


class TaskManager:
    def __init__(self, gui):
        '''функция-конструктор менеджера задач(класс для загрузки и парсинга задач)
        ,принимает gui, куда нужно выводить текст задач, ничего не возвращает'''
        self.gui_class = gui
        self.current_task_index = 0
        self.tasks = ["Выберите файл, пожалуйста, но можно печатать и это"]
        self.text_to_type = ""
        self.current_chunk = ""  # делю большой текст на части, это текст части текста

        self.chunks = [self.text_to_type[i:i + Globals.chunk_size] for i in
                       range(0, len(self.text_to_type), Globals.chunk_size)]

    def load_task(self):
        '''функция для вывода текста в gui, ничего не принимает, ничего не возвращает'''
        if self.current_task_index < len(self.tasks):
            self.text_to_type = self.tasks[self.current_task_index]
            self.chunks = [self.text_to_type[i:i + Globals.chunk_size] for i in
                           range(0, len(self.text_to_type), Globals.chunk_size)]
            self.gui_class.text_label.config(text=self.chunks[0])
            self.gui_class.entry.config(state=tk.NORMAL)
            self.gui_class.clear_entry()
        else:
            self.text_to_type = ""
            self.gui_class.text_label.config(text="Задания завершены")
            self.gui_class.clear_entry()
            self.gui_class.show_stats_button.config(state=tk.NORMAL)
            self.gui_class.show_heatmap_button.config(state=tk.NORMAL)

    def load_next_task(self):
        '''функция для загрузки следующего задания(она нужна, т.к иногда не нужно увеличивать индекс задачи
        , ничего не принимает, ничего не возвращает'''
        self.current_task_index += 1
        self.load_task()
