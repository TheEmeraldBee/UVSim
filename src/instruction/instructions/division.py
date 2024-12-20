from src.instruction.instruction import Instruction
from typing import Optional

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.vm.virtual_machine import VirtualMachine
    from src.tab.run import RunTab

from src.instruction.event import InstructionEvent


class DivisionInstruction(Instruction):
    """Divides the accumulator by a memory value in an integer"""
    instruction = 32

    def __init__(self):
        pass

    def handle(
        self, vm: "VirtualMachine", address: int, output: "RunTab"
    ) -> Optional["InstructionEvent"]:
        vm.accumulator = vm.accumulator // vm.get_memory().get(address)
        return
