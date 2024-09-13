from src.instruction.instruction import Instruction
from src.vm.virtual_machine import VirtualMachine


class BranchInstruction(Instruction):
    instruction = 40

    def __init__(self):
        pass

    def handle(self, vm: VirtualMachine, address: int):
        vm.cpu.set_program_location(address)

