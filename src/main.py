from src.tab.tabs import Tabs
import tkinter as tk
from tkinter import ttk
from src.config.color_config import ColorConfig


class Main:
    """Main Class for the program""" 

    def __init__(self):
        """Build the program"""
        self.color_config = ColorConfig()

        # Main window
        self.root = tk.Tk()
        self.root.title("UV Sim")

        Tabs(self, self.root, self.color_config, False)
        
    def new_sub_window(self):
        Tabs(self, self.root, self.color_config)

    def run(self):
        self.root.mainloop() 


if __name__ == "__main__":
    Main().run()
