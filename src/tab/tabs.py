import tkinter as tk
from tkinter import ttk
from src.tab.editor import EditorTab
from src.tab.run import RunTab


class Tabs:
    def __init__(self, main, root, color_config, top_level = True):
        if top_level:
            self.window = tk.Toplevel(root)
            self.window.title("New Tab")
        else:
            self.window = root

        self.root = root
        
        self.tabs = []
        self.color_config = color_config

        border_frame = tk.Frame(self.window, bg=self.color_config.primary_color, padx=15, pady=15)
        border_frame.pack(fill="both", expand=True)

        # Inner content frame
        content_frame = tk.Frame(border_frame, bg=self.color_config.secondary_color, padx=5, pady=5)
        content_frame.pack(fill="both", expand=True)

        self.tab_root = ttk.Notebook(content_frame)
        self.tab_root.pack(expand=True, fill="both")

        self.editor_tab = EditorTab(self.new_tab("Editor"), self.color_config)
        self.run_tab = RunTab(self.new_tab("Running"), self.color_config)

        # Buttons frame at the bottom of the window
        button_frame = tk.Frame(content_frame)
        button_frame.pack(side=tk.BOTTOM)

        # "New Tab" button
        new_tab_button = ttk.Button(button_frame, text="New Tab", command=main.new_sub_window)
        new_tab_button.pack(side=tk.LEFT, padx=5)

        # "Settings" button
        settings_button = ttk.Button(button_frame, text="Settings", command=self.open_settings)
        settings_button.pack(side=tk.LEFT, padx=5)

    def new_tab(self, name):
        tab = ttk.Frame(self.tab_root, style="Custom.TFrame")
        self.tab_root.add(tab, text=name)
        self.tabs.append(tab)
        return tab
    
    def pack(self):
        self.tab_root.pack(fill=tk.BOTH, expand=1)

    def open_settings(self):
        from src.tab.settings import SettingsWindow
        SettingsWindow(self.window, self.color_config, self.apply_colors)

    def apply_colors(self):
        self.root.configure(bg=self.color_config.primary_color)
