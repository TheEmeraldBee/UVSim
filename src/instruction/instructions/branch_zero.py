from src.instruction.instruction import Instruction

from typing import Optional

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.vm.virtual_machine import VirtualMachine
from src.instruction.event import InstructionEvent

class BranchZeroInstruction(Instruction):
    instruction = 42

    def __init__(self):
        pass

    def handle(self, vm: 'VirtualMachine', address: int, output) -> Optional['InstructionEvent']:
        if vm.accumulator == 0: 
            vm.cpu.set_program_location(address)
        return
        


