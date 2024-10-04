from abc import ABC, abstractmethod
from typing import Optional

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.vm.virtual_machine import VirtualMachine
    from src.instruction.event import InstructionEvent


class Instruction(ABC):

    @property
    @abstractmethod
    def instruction(self):
        """The value of the instruction that will be checked by the cpu to interpret this instruction."""
        ...

    @abstractmethod
    def handle(
        self, vm: "VirtualMachine", address: int, output
    ) -> Optional["InstructionEvent"]:
        """Handle the instruction with only the VM and ADDRESS"""
        ...
