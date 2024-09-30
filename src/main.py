from src.tab.editor import EditorTab
from src.tab.run import RunTab
from src.tab.tabs import Tabs
import tkinter


class Main:
    """Main Class for the program"""

    def __init__(self):
        """Build the program"""
        self.root = tkinter.Tk()
        self.root.title("UV Sim")

        self.tabs = Tabs(self.root)
        self.editor_tab = EditorTab(self.tabs.new_tab("Editor"))
        self.run_tab = RunTab(self.tabs.new_tab("Running"))
        self.tabs.pack()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    Main().run()
