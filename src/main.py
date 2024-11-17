from src.tab.editor import EditorTab
from src.tab.run import RunTab
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
        
        # Main border frame
        border_frame = tk.Frame(self.root, bg=self.color_config.primary_color, padx=15, pady=15)
        border_frame.pack(fill="both", expand=True)

        # Inner content frame
        content_frame = tk.Frame(border_frame, bg=self.color_config.secondary_color, padx=5, pady=5)
        content_frame.pack(fill="both", expand=True)

        # Initialize tabs
        self.tabs = Tabs(content_frame, color_config=self.color_config)
        self.tabs.pack()

        self.editor_tab = EditorTab(self.tabs.new_tab("Editor"), self.color_config)
        self.run_tab = RunTab(self.tabs.new_tab("Running"), self.color_config)

        # Buttons frame at the bottom of the window
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        # "New Tab" button
        new_tab_button = ttk.Button(button_frame, text="New Tab", command=self.tabs.create_dynamic_run_tab)
        new_tab_button.pack(side=tk.LEFT, padx=5)

        # "Settings" button
        settings_button = ttk.Button(button_frame, text="Settings", command=self.open_settings)
        settings_button.pack(side=tk.LEFT, padx=5)


    def open_settings(self):
        from src.tab.settings import SettingsWindow
        SettingsWindow(self.root, self.color_config, self.apply_colors)

    def apply_colors(self):
        self.root.configure(bg=self.color_config.primary_color)

    def run(self):
        self.root.mainloop() 


if __name__ == "__main__":
    Main().run()
