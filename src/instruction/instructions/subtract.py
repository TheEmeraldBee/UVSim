from src.instruction.instruction import Instruction

from typing import Optional

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.vm.virtual_machine import VirtualMachine
from src.instruction.event import InstructionEvent

class SubtractInstruction(Instruction):
    instruction = 31

    def __init__(self):
        pass

    def handle(self, vm: 'VirtualMachine', address: int) -> Optional['InstructionEvent']:
        vm.accumulator -= vm.get_memory().get(address)
        return
