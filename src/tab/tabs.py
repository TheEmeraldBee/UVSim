import tkinter as tk
from tkinter import ttk
from src.tab.dynamic_run_tab import DynamicRunTab

MAX_TABS = 5

class Tabs:
    def __init__(self, root, color_config): 
        self.tab_root = ttk.Notebook(root)
        self.tabs = []
        self.color_config = color_config

    def new_tab(self, name):
        tab = ttk.Frame(self.tab_root, style="Custom.TFrame")
        self.tab_root.add(tab, text=name)
        self.tabs.append(tab)
        return tab
    
    def create_dynamic_run_tab(self):
        """Creates a new tab with the Running tab's layout"""
        if len(self.tabs) >= MAX_TABS:
            print("Max number of tabs reached.")
            return

        name = f"New Tab {len(self.tabs) + 1}"
        DynamicRunTab(name, self, self.color_config)

    def pack(self):
        self.tab_root.pack(fill=tk.BOTH, expand=1)
