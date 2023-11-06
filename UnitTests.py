import unittest
from tkinter import Tk
from unittest.mock import Mock
import pandas as pd

from src.FileManager import load_data, save_data
from src.Stats import StatClass
from src.Globals import Globals
from src.TaskManager import TaskManager

class TestFileManager(unittest.TestCase):
    def test_load_data(self):
        data = load_data()
        self.assertIsNotNone(data)
        self.assertIsInstance(data, pd.DataFrame)

    def test_save_data(self):
        data = pd.DataFrame({'Character': Globals.allowed_characters, 'Count': 5})
        save_data(data)
        loaded_data = load_data()
        self.assertIsNotNone(loaded_data)
        self.assertIsInstance(loaded_data, pd.DataFrame)
        self.assertTrue(loaded_data.equals(data))

class TestStatClass(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.task_manager = TaskManager(self.root)
        self.gui = None
        self.stat_class = StatClass(self.task_manager, self.gui)

    def tearDown(self):
        self.root.destroy()

    def test_clear_stats(self):
        self.stat_class.errors = 10
        self.stat_class.prev_errors = 5
        self.stat_class.clear_stats()
        self.assertEqual(self.stat_class.errors, 0)
        self.assertEqual(self.stat_class.prev_errors, 10)

if __name__ == '__main__':
    unittest.main()
