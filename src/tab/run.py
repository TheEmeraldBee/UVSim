import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

from src.vm.virtual_machine import *


class RunTab:
    def __init__(self, root, color_config):
        self.root = root

        self.paused = False

        self.commands = tk.Frame(root, bg=color_config.primary_color)
        self.open_button = tk.Button(self.commands, text="Open", command=self.open, bg=color_config.secondary_color, fg="black")
        self.run_button = tk.Button(self.commands, text="Run", command=self.run, bg=color_config.secondary_color, fg="black")
        self.update_memory_button = tk.Button(self.commands, text="Update Memory", command=self.update_memory, bg=color_config.secondary_color, fg="black")

        self.open_button.grid(column=0, row=0)
        self.run_button.grid(column=1, row=0)
        self.update_memory_button.grid(column=2, row=0)

        self.commands.pack()

        # Left window colors
        text_border_frame = tk.Frame(root, bg=color_config.primary_color, padx=5, pady=5)
        text_border_frame.pack(side=tk.LEFT, padx=10, pady=10, fill="both", expand = True)
        self.text_area = tk.Text(text_border_frame, state=tk.DISABLED, bg=color_config.secondary_color, fg="black")
        self.text_area.pack(fill="both", expand=True)

        # Input box color
        self.num_input = tk.Entry(text_border_frame, state=tk.DISABLED, bg=color_config.secondary_color, fg="black")
        self.num_input.pack()


        # Right window colors 
        memory_border_frame = tk.Frame(root, bg=color_config.primary_color, padx=5, pady=5)
        memory_border_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill="both", expand = True)
        self.memory_area = tk.Text(memory_border_frame, state=tk.DISABLED, bg=color_config.secondary_color, fg="black")
        self.memory_area.pack(fill="both", expand=True) 

        self.vm = VirtualMachine()
        self.update_memory()

    def open(self):
        path = filedialog.askopenfilename(title="File to load", initialdir="./")
        self.vm.get_memory().load_file(path)
        self.update_memory()

    def run(self) -> None:
        if self.paused:
            self.root.after(10, self.run)
            return

        result = self.vm.step(self)
        self.update_memory()
        if result:
            self.root.after(10, self.run)

    def update_memory(self):
        memory = self.vm.get_memory()

        # Iterate through memory locations, and add entries to the frame
        text = ""

        for i in range(0, MEMORY_SIZE):
            text += f"{i:2} ---------- {memory.get(i)}\n"

        self.memory_area.config(state=tk.NORMAL)
        self.memory_area.replace("1.0", tk.END, text)
        self.memory_area.config(state=tk.DISABLED)
    
  
