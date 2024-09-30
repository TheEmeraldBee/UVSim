from tkinter import ttk
from tkinter import filedialog

import tkinter as tk


class EditorTab:
    def __init__(self, root):
        self.text = tk.Text(root)
        self.scroll_bar = ttk.Scrollbar(root)

        self.text.configure(yscrollcommand=self.scroll_bar.set)
        self.scroll_bar.config(command=self.text.yview)

        self.commands = ttk.Frame(root)

        self.open_button = ttk.Button(self.commands, text="Open", command=self.open)
        self.open_button.grid(column=0, row=0)

        self.save_button = ttk.Button(self.commands, text="Save", command=self.save)
        self.save_button.grid(column=1, row=0)

        # Pack Widgets
        self.commands.pack(anchor=tk.NW)
        self.scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def open(self):
        path = filedialog.askopenfilename(initialdir="./", defaultextension=".txt")
        if path == "":
            return

        with open(path, "r") as file:
            data = file.read()
            self.text.replace("1.0", tk.END, data)
            self.text.update()

    def save(self):
        path = filedialog.asksaveasfilename(initialdir="./", defaultextension=".txt")
        if path == "":
            return
        with open(path, "w") as file:
            file.write(self.text.get("1.0", tk.END))
