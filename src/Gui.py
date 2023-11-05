import tkinter as tk
from src.PrintChecker import PrintChecker
from src.Stats import StatClass
from src.FileManager import FileManager
from src.TaskManager import TaskManager
from src.StatVisual import StatVisualization
from src.StatVisual import show_stats


class GUI:
    def __init__(self, root):
        '''функция конструктор объекта класса GUI, принимает Окно tkinter, ничего не возвращает'''
        self.task_class = TaskManager(gui=self)
        self.file_manager = FileManager(task_class=self.task_class)
        self.stat_class = StatClass(task_manager=self.task_class, gui=self)
        self.print_checker = PrintChecker(stat_class=self.stat_class, gui_class=self, task_manager=self.task_class,
                                          file_manager=self.file_manager)
        self.stat_vis_class = StatVisualization(stat_class=self.stat_class)
        self.root = root
        self.root.title("Клавиатурный тренажёр")

        self.text_label = tk.Label(root, text="", font=("Helvetica", 14), width=50, anchor=tk.W)
        self.text_label.pack(pady=20)

        self.entry = tk.Entry(root, font=("Helvetica", 14), width=50, state=tk.DISABLED)
        self.entry.pack()
        self.entry.bind("<Key>", lambda event: self.print_checker.check_key(event))

        self.stats_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.stats_label.pack(pady=10)

        self.clear_history_button = tk.Button(root, text="Очистить историю статистики",
                                              command=self.stat_class.clear_stat_history)
        self.clear_history_button.pack()

        self.show_stats_button = tk.Button(root, text="Показать статистику", command=show_stats)
        self.show_stats_button.pack()
        self.show_stats_button.config(state=tk.DISABLED)

        self.show_heatmap_button = tk.Button(root, text="Показать heatmap",
                                             command=self.stat_vis_class.create_key_heatmap)
        self.show_heatmap_button.pack()
        self.show_heatmap_button.config(state=tk.DISABLED)

        self.load_tasks_button = tk.Button(root, text="Загрузить задания",
                                           command=self.file_manager.load_tasks_from_file)
        self.load_tasks_button.pack()

        self.task_class.load_task()

    def clear_entry(self):
        '''функция очистки окна ввода, ничего не принимает, ничего не возвращает'''
        self.entry.delete(0, tk.END)
