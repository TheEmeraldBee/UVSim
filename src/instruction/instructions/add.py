from typing import Optional
from typing import TYPE_CHECKING

from src.instruction.instruction import Instruction

if TYPE_CHECKING:
    from src.vm.virtual_machine import VirtualMachine
    from src.tab.run import RunTab

from src.instruction.event import InstructionEvent


class AddInstruction(Instruction):
    """Represents an addition instruction for the virtual machine."""
    instruction = 30

    def __init__(self):
        pass

    def handle(
        self, vm: "VirtualMachine", address: int, output: "RunTab"
    ) -> Optional["InstructionEvent"]:
        vm.accumulator += vm.get_memory().get(address)
        return
