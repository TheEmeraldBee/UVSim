from src.instruction.instruction import Instruction
from src.vm.virtual_machine import VirtualMachine

class DivisionInstruction(Instruction):
    instruction = 32

    def __init__(self):
        pass

    def handle(self, vm: VirtualMachine, address: int):
        vm.accumulator = vm.accumulator // vm.get_memory().get(address)