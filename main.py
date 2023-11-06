import tkinter as tk
import os
from src.Gui import GUI

if __name__ == "__main__":
    data_folder = "data"
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
    root = tk.Tk()
    trainer = GUI(root)
    root.mainloop()
