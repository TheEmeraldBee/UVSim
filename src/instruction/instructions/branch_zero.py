from src.instruction.instruction import Instruction

from typing import Optional

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.vm.virtual_machine import VirtualMachine
    from src.tab.run import RunTab

from src.instruction.event import InstructionEvent

class BranchZeroInstruction(Instruction):
    """Handles branch operations when the accumulator is zero."""

    instruction = 42

    def __init__(self):
        pass

    def handle(self, vm: 'VirtualMachine', address: int, output: "RunTab") -> Optional['InstructionEvent']:
        if vm.accumulator == 0: 
            vm.cpu.set_program_location(address)
            return InstructionEvent.NO_ADVANCE
        return
        


