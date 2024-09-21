import platform

if platform.system() == "Windows":
    from msvcrt import getch
else:
    import getch

from src.instruction.instruction import Instruction

from typing import Optional

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.vm.virtual_machine import VirtualMachine
from src.instruction.event import InstructionEvent


class ReadInstruction(Instruction):
    instruction = 10

    def __init__(self):
        pass

    def handle(
        self, vm: "VirtualMachine", address: int
    ) -> Optional["InstructionEvent"]:
        vm.get_memory().set(address, ord(getch.getch()))
        return
