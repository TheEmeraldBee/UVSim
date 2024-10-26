from src.tab.editor import EditorTab
from src.tab.run import RunTab
from src.tab.tabs import Tabs
import tkinter
from src.config.color_config import ColorConfig
from tkinter import ttk

class Main:
    """Main Class for the program""" 

    def __init__(self):
        """Build the program"""
        self.color_config = ColorConfig()

        self.root = tkinter.Tk()
        self.root.title("UV Sim")
        
        # Main border frame
        border_frame = tkinter.Frame(self.root, bg=self.color_config.primary_color, padx=15, pady=15)
        border_frame.pack(fill="both", expand=True)
        content_frame = tkinter.Frame(border_frame, bg=self.color_config.secondary_color, padx=5, pady=5)
        content_frame.pack(fill="both", expand=True)
        self.tabs = Tabs(content_frame, color_config=self.color_config)
        self.editor_tab = EditorTab(self.tabs.new_tab("Editor"), self.color_config)
        self.run_tab = RunTab(self.tabs.new_tab("Running"), self.color_config)

        settings_button = ttk.Button(self.root, text="Settings", command=self.open_settings)
        settings_button.pack(pady=10)

        self.tabs.pack()

    def open_settings(self):
        from src.tab.settings import SettingsWindow
        SettingsWindow(self.root, self.color_config, self.apply_colors)

    def apply_colors(self):
        self.root.configure(bg=self.color_config.primary_color)

    def run(self):
        self.root.mainloop() 


if __name__ == "__main__":
    Main().run()
