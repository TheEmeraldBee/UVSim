from typing import Optional
from typing import TYPE_CHECKING
import tkinter as tk

from src.instruction.instruction import Instruction

if TYPE_CHECKING:
    from src.vm.virtual_machine import VirtualMachine
    from src.tab.run import RunTab

from src.instruction.event import InstructionEvent


class WriteInstruction(Instruction):
    instruction = 11

    def __init__(self):
        pass

    def handle(
        self, vm: "VirtualMachine", address: int, output: "RunTab"
    ) -> Optional["InstructionEvent"]:
        output.text_area.configure(state=tk.NORMAL)
        output.text_area.insert(tk.END, str(chr(vm.get_memory().get(address))))
        output.text_area.configure(state=tk.DISABLED)
        return