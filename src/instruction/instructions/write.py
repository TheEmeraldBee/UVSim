from typing import Optional
from typing import TYPE_CHECKING
import tkinter as tk

from src.instruction.instruction import Instruction

if TYPE_CHECKING:
    from src.vm.virtual_machine import VirtualMachine

from src.instruction.event import InstructionEvent


class WriteInstruction(Instruction):
    instruction = 11

    def __init__(self):
        pass

    def handle(
        self, vm: "VirtualMachine", address: int, output
    ) -> Optional["InstructionEvent"]:
        #output.append( chr(vm.get_memory().get(address)))
        output.insert(tk.END, chr(vm.get_memory().get(address)))
        output.update()
        return
