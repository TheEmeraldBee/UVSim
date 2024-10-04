from src.instruction.event import InstructionEvent
from src.instruction.instruction import Instruction

from typing import Optional

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.vm.virtual_machine import VirtualMachine

class HaltInstruction(Instruction):
    instruction = 43

    def __init__(self):
        pass

    def handle(self, vm: 'VirtualMachine', address: int, output) -> Optional['InstructionEvent']:
        return InstructionEvent.QUIT