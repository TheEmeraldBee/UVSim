from src.instruction.event import InstructionEvent
from src.instruction.instruction import Instruction

from typing import Optional

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.vm.virtual_machine import VirtualMachine
    from src.tab.run import RunTab

class HaltInstruction(Instruction):
    """Halts the execution of the virtual machine"""
    instruction = 43

    def __init__(self):
        pass

    def handle(self, vm: 'VirtualMachine', address: int, output: "RunTab") -> Optional['InstructionEvent']:
        return InstructionEvent.QUIT