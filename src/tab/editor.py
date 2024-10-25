from tkinter import ttk
from tkinter import filedialog

import tkinter.messagebox as msg

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

        self.validate_button = ttk.Button(
            self.commands, text="Validate", command=self.validate
        )
        self.validate_button.grid(column=2, row=0)

        # Pack Widgets
        self.commands.pack(anchor=tk.NW)
        self.scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def validate(self):
        # Read text from textbox
        text = self.text.get("1.0", tk.END)

        line_idx = 1
        valid = True
        lines = text.splitlines()

        # Ensure line count is less than 100
        if len(lines) > 100:
            msg.showwarning(
                title="Invalid Program",
                message=f"Program is invalid, it contains more than 100 instructions, which would overflow memory",
            )
            valid = False

        for line in text.splitlines():
            # Ignore Empty Lines when Validating
            if line.strip() == "":
                continue

            # Ensure line starts with sign
            if line[0] != "+" and line[0] != "-":
                msg.showwarning(
                    title="Invalid Instruction",
                    message=f"Line {line_idx} Is invalid, first character should be a + or -",
                )
                valid = False

            try:
                # Convert Remaining text in line to an integer
                num = int(line[1::])

                # Ensure value of instruction is valid
                if num != 0 and len(line[1::]) != 4:
                    msg.showwarning(
                        title="Invalid Instruction",
                        message=f"Line {line_idx} Is invalid, instruction value should either be `0` or be 4 digits long",
                    )
                    valid = False
            except ValueError:
                # Value of instruction was not an integer, therefore invalid
                msg.showwarning(
                    title="Invalid Instruction",
                    message="Line {line_idx} Is invalid, after `+` or `-`, a number should follow",
                )
                valid = False

            # Increment a Line Index for information on where errors are.
            line_idx += 1

        # Show that code was validated if no errors were found.
        if valid:
            msg.showinfo(title="Code Validated", message="No Warnings Or Errors Found.")

    def open(self) -> None:
        path = filedialog.askopenfilename(initialdir="./", defaultextension=".txt")
        if path == "":
            return

        with open(path, "r") as file:
            data = file.read()
            self.text.replace("1.0", tk.END, data)
            self.text.update()

    def save(self) -> None:
        path = filedialog.asksaveasfilename(initialdir="./", defaultextension=".txt")
        if path == "":
            return
        with open(path, "w") as file:
            file.write(self.text.get("1.0", tk.END))
