from abc import ABC, abstractmethod

from src.vm.virtual_machine import VirtualMachine

class Instruction(ABC):

    @property
    @abstractmethod
    def instruction(self):
        """The value of the instruction that will be checked by the cpu to interpret this instruction."""
        ...

    @abstractmethod
    def handle(self, vm: VirtualMachine, address: int):
        """Handle the instruction with only the VM and ADDRESS"""
        ...