from src.instruction.instruction import Instruction

from typing import Optional

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.vm.virtual_machine import VirtualMachine
from src.instruction.event import InstructionEvent

class StoreInstruction(Instruction):
    instruction = 21

    def __init__(self):
        pass

    def handle(self, vm: 'VirtualMachine', address: int) -> Optional['InstructionEvent']:
        vm.get_memory().set(address, vm.accumulator)
        return