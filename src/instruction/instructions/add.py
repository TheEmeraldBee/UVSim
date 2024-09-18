from typing import Optional
from typing import TYPE_CHECKING

from src.instruction.instruction import Instruction

if TYPE_CHECKING:
    from src.vm.virtual_machine import VirtualMachine

from src.instruction.event import InstructionEvent


class AddInstruction(Instruction):
    instruction = 30

    def __init__(self):
        pass

    def handle(
        self, vm: "VirtualMachine", address: int
    ) -> Optional["InstructionEvent"]:
        vm.accumulator += vm.get_memory().get(address)
        return
