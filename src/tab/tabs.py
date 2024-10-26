import tkinter as tk
from tkinter import ttk

class Tabs:
    def __init__(self, root, color_config): 
        self.tab_root = ttk.Notebook(root)
        self.tabs = []
        self.color_config = color_config

    def new_tab(self, name):
        self.tabs += [ttk.Frame(self.tab_root)]
        tab = ttk.Frame(self.tab_root, style="Custom.TFrame")
        self.tab_root.add(tab, text=name)
        return tab

    def pack(self):
        self.tab_root.pack(fill=tk.BOTH, expand=1)
