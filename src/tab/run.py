import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

from src.vm.virtual_machine import VirtualMachine


class RunTab:
    def __init__(self, root):
        self.label = tk.Label(root, text="Running Code")

        self.commands = ttk.Frame(root)

        self.open_button = ttk.Button(self.commands, text="Open", command=self.open)
        self.run_button = ttk.Button(self.commands, text="Run", command=self.run)
        self.update_memory_button = ttk.Button(
            self.commands, text="Update Memory", command=self.update_memory
        )

        self.open_button.grid(column=0, row=0)
        self.run_button.grid(column=1, row=0)
        self.update_memory_button.grid(column=2, row=0)

        self.commands.pack(anchor=tk.NW)

        self.input_area = tk.Text(root, state=tk.DISABLED)
        self.input_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.memory_area = tk.Text(root, state=tk.DISABLED)

        self.memory_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.vm = VirtualMachine()

    def open(self):
        path = filedialog.askopenfilename(title="File to load", initialdir="./")
        self.vm.get_memory().load_file(path)

    def run(self):
        while self.vm.step():
            self.update_memory()

    def update_memory(self):
        memory = self.vm.get_memory()

        # Iterate through memory locations, and add entries to the frame
        text = ""

        for i in range(0, 100):
            text += f"{i:2} ---------- {memory.get(i)}\n"

        self.memory_area.replace("1.0", tk.END, text)
