from src.instruction.instruction import Instruction

from typing import Optional

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.vm.virtual_machine import VirtualMachine
    from src.tab.run import RunTab

from src.instruction.event import InstructionEvent

class StoreInstruction(Instruction):
    """Stores the value from the accumulator into memory at the given address"""
    instruction = 21

    def __init__(self):
        pass

    def handle(self, vm: 'VirtualMachine', address: int, output: "RunTab") -> Optional['InstructionEvent']:
        vm.get_memory().set(address, vm.accumulator)
        return