from src.instruction.instruction import Instruction

from typing import Optional

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.vm.virtual_machine import VirtualMachine
    from src.tab.run import RunTab

from src.instruction.event import InstructionEvent


class BranchInstruction(Instruction):
    """Handles unconditional branching to a specified memory address."""
    instruction = 40

    def __init__(self):
        pass

    def handle(
        self, vm: "VirtualMachine", address: int, output: "RunTab"
    ) -> Optional["InstructionEvent"]:
        vm.cpu.set_program_location(address)
        return InstructionEvent.NO_ADVANCE
