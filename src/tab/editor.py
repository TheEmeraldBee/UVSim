from tkinter import ttk
from tkinter import filedialog

import tkinter.messagebox as msg

import tkinter as tk 

from src.vm.virtual_machine import MEMORY_SIZE
from src.instruction.parsed_instruction import INSTRUCTION_CODE_LENGTH

class EditorTab:
    """Class to manage the text editor tab with various functionality like open, save, validate, and more"""
    def __init__(self, root, color_config):
        # Command frame for buttons (keeping buttons white)
        self.commands = tk.Frame(root, bg=color_config.primary_color)
        self.open_button = tk.Button(self.commands, text="Open", command=self.open, bg=color_config.secondary_color, fg="black")
        self.open_button.grid(column=0, row=0)

        self.save_button = tk.Button(self.commands, text="Save", command=self.save, bg=color_config.secondary_color, fg="black")
        self.save_button.grid(column=1, row=0)

        self.validate_button = tk.Button(self.commands, text="Validate", command=self.validate, bg=color_config.secondary_color, fg="black")
        self.validate_button.grid(column=2, row=0)

        self.validate_button = tk.Button(self.commands, text="Convert Command", command=self.convert, bg=color_config.secondary_color, fg="black")
        self.validate_button.grid(column=3, row=0)
        
        self.cut_button = tk.Button(self.commands, text="Cut", command=self.cut, bg=color_config.secondary_color, fg="black")
        self.cut_button.grid(column=4, row=0)

        self.copy_button = tk.Button(self.commands, text="Copy", command=self.copy, bg=color_config.secondary_color, fg="black")
        self.copy_button.grid(column=5, row=0)

        self.paste_button = tk.Button(self.commands, text="Paste", command=self.paste, bg=color_config.secondary_color, fg="black")
        self.paste_button.grid(column=6, row=0)

        self.commands.pack(anchor=tk.NW) # Packs command buttons at the top

        # Outer border frame for the main text area
        text_border_frame = tk.Frame(root, bg=color_config.primary_color, padx=5, pady=5)
        text_border_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Main text area inside the border frame
        self.text = tk.Text(text_border_frame, bg=color_config.secondary_color, fg="black")
        self.scroll_bar = ttk.Scrollbar(root)

        self.text.configure(yscrollcommand=self.scroll_bar.set)
        self.scroll_bar.config(command=self.text.yview)
        self.scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text.pack(fill="both", expand=True)  # Ensure text fills within border
        
    def cut(self) -> None:
        """Cuts the selected text to the clipboard."""
        self.text.event_generate("<<Cut>>")

    def copy(self) -> None:
        """Copies the selected text to the clipboard."""
        self.text.event_generate("<<Copy>>")

    def paste(self) -> None:
        """Pastes the text from the clipboard into the editor."""
        self.text.event_generate("<<Paste>>")

    def validate(self):
        """Validates the text in the editor making sure it is valid."""
        # Read text from textbox
        text = self.text.get("1.0", tk.END)

        line_idx = 1
        valid = True
        lines = text.splitlines()

        # Ensure line count is less than 100
        if len(lines) > MEMORY_SIZE:
            msg.showwarning(
                title="Invalid Program",
                message="Program is invalid, it contains more than 100 instructions, which would overflow memory",
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
                _ = int(line[1::])

                # Ensure value of instruction is valid
                if len(line[1::]) != (INSTRUCTION_CODE_LENGTH * 2):
                    msg.showwarning(
                        title="Invalid Instruction",
                        message=f"Line {line_idx} Is invalid, instruction value should be {INSTRUCTION_CODE_LENGTH * 2} digits long",
                    )
                    valid = False

                op_code = int(line[1:4:])
                addr = int(line[4::])
                if addr > MEMORY_SIZE or op_code > MEMORY_SIZE:
                    msg.showwarning(
                        title="Invalid Instruction",
                        message=f"Line {line_idx} is invalid. both halves of instruction should be betweeen 0 and {MEMORY_SIZE}"
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
    
     
    def convert(self) -> None: 
        """"converts commands from 5 digits to 7."""
        text = self.text.get("1.0", tk.END)
        lines = text.splitlines()
        for line in range(len(lines)): 
            if len(lines[line]) == 5: 
                partOne = lines[line][1:3]
                partTwo = lines[line][3::]
                alteredCommand = f"{lines[line][0]}0{partOne}0{partTwo}"
                lines[line] = alteredCommand
        lines = "\n".join(lines)
        self.text.replace("1.0", tk.END, lines)

