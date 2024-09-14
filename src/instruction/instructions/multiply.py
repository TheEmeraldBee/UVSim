from src.instruction.instruction import Instruction
from src.vm.virtual_machine import VirtualMachine


class MultiplyInstruction(Instruction):
    instruction = 33

    def __init__(self):
        pass

    def handle(self, vm: VirtualMachine, address: int):
        vm.accumulator *= vm.get_memory().get(address)
