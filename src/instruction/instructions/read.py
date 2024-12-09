import tkinter as tk


from src.instruction.instruction import Instruction

from typing import Optional

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.vm.virtual_machine import VirtualMachine
    from src.tab.run import RunTab
from src.instruction.event import InstructionEvent


class ReadInstruction(Instruction):
    """Handles user input to read a value and store it in memory"""
    instruction = 10

    def __init__(self):
        pass

    def handle(
        self, vm: "VirtualMachine", address: int, output: "RunTab"
    ) -> Optional["InstructionEvent"]:
        output.num_input.configure(state=tk.NORMAL)

        self.output = output
        self.output.paused = True
        self.vm = vm
        self.address = address
        output.num_input.bind("<Return>", self.end_read)

        return

    def end_read(self, event) -> Optional["InstructionEvent"]:
        try:
            val = int(self.output.num_input.get())
        except ValueError:
            self.output.text_area.configure(state=tk.NORMAL)
            self.output.text_area.insert(
                tk.END,
                f"\nInput {self.output.num_input.get()} is invalid. Please type a positive number\n",
            )
            self.output.num_input.delete(0, tk.END)
            self.output.text_area.configure(state=tk.DISABLED)
            return

        self.output.paused = False
        self.vm.get_memory().set(self.address, val)
        self.output.num_input.delete(0, tk.END)
        self.output.num_input.configure(state=tk.DISABLED)
        self.output.root.unbind("<Return>")
