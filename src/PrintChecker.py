import tkinter as tk
import time
from src.Globals import Globals
from src.FileManager import save_data


class PrintChecker:
    def __init__(self, stat_class, gui_class, task_manager, file_manager):
        '''Функция-конструктор класса проверки вводимых сивмолов,
        принимает класс статистики для её изменения,
        класс gui для изменения в некоторых случаях и не позволения вводить неверные символы
        класс менеджера заданиями для того, чтобы знать, что вводить и какой символ верный
        класс менеджера файлов для сохранения измененной статистики
        ничего не возвращает'''
        self.file_manager = file_manager
        self.stat_class = stat_class
        self.gui_class = gui_class
        self.task_manager = task_manager
        self.chunk_index = 0
        self.last_error_position = None  # нужен, чтобы две ошибки на одном месте не считалось за 2 ошибки
        self.text_index = 0  # номер текста, который нужно печатать
        self.start = True  # Бул для отслеижвания старта программы

    def check_key(self, event):
        '''Главная функция программы для проверки вводимых символов, принимает tk.Event(событие клавиш), ничего не возращает'''
        if event.keysym == 'BackSpace':
            return "break"
        input_char = event.char
        if input_char not in Globals.allowed_characters:
            return

        if self.start:
            self.gui_class.clear_history_button.config(state=tk.DISABLED)
            self.start = False

        if not self.stat_class.typing:
            self.stat_class.typing = True
            self.stat_class.start_time = time.time()

        if self.text_index == 0:
            self.gui_class.clear_entry()

        if self.chunk_index < len(self.task_manager.chunks):
            if input_char.isalpha() or input_char.isspace() or input_char in '.,-!?()[]{}' or input_char in '0123456789':
                if self.chunk_index < len(self.task_manager.chunks) \
                        and self.text_index < len(self.task_manager.chunks[self.chunk_index]) \
                        and input_char == self.task_manager.chunks[self.chunk_index][self.text_index]:
                    self.text_index += 1
                    self.stat_class.characters_typed += 1
                    self.last_error_position = None
                else:
                    if self.last_error_position != self.text_index:
                        self.stat_class.errors += 1
                        char = self.task_manager.chunks[self.chunk_index][self.text_index - 1]
                        self.stat_class.error_keys.loc[self.stat_class.error_keys['Character'] == char, 'Count'] += 1
                        self.last_error_position = self.text_index

                    return "break"

            if self.text_index == len(self.task_manager.chunks[self.chunk_index]):
                if self.chunk_index == (len(self.task_manager.chunks) - 1):
                    self.gui_class.entry.insert(tk.END, input_char)
                self.text_index = 0
                self.chunk_index += 1

                if self.chunk_index < len(self.task_manager.chunks):
                    self.gui_class.text_label.config(text=self.task_manager.chunks[self.chunk_index])
                else:
                    self.end_typing()
        self.stat_class.update_stats_label()

    def end_typing(self):
        '''Функция для обработки конца задания, ничего не принимает, ничего не возращает'''
        self.text_index = 0
        self.last_error_position = None
        self.stat_class.characters_typed = 0
        self.stat_class.typing = False
        self.gui_class.entry.config(state=tk.DISABLED)
        self.file_manager.save_stats_to_file(False, self.stat_class.typing_speed)
        self.gui_class.root.after(100, self.task_manager.load_next_task())
        self.chunk_index = 0
        self.stat_class.clear_stats()
        if self.task_manager.current_task_index == len(self.task_manager.tasks):
            save_data(self.stat_class.error_keys)

