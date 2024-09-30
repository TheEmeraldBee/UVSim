import tkinter as tk
from tkinter import ttk


class Tabs:
    def __init__(self, root):
        self.tab_root = ttk.Notebook(root)
        self.tabs = []

    def new_tab(self, name):
        self.tabs += [ttk.Frame(self.tab_root)]
        tab = self.tabs[len(self.tabs) - 1]

        self.tab_root.add(tab, text=name)

        return tab

    def pack(self):
        self.tab_root.pack(fill=tk.BOTH, expand=1)
