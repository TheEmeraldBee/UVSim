from src.instruction.instruction import Instruction

from typing import Optional

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.vm.virtual_machine import VirtualMachine
    from src.tab.run import RunTab
from src.instruction.event import InstructionEvent

class LoadInstruction(Instruction):
    """Loads a value from memory into the accumulator"""
    instruction = 20

    def __init__(self):
        pass

    def handle(self, vm: 'VirtualMachine', address: int, output: "RunTab") -> Optional['InstructionEvent']:
        vm.accumulator = vm.get_memory().get(address)
        return