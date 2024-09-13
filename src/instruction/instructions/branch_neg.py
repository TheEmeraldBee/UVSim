from src.instruction.instruction import Instruction
from src.vm.virtual_machine import VirtualMachine


class BranchNegInstruction(Instruction):
    instruction = 41

    def __init__(self):
        pass

    def handle(self, vm: VirtualMachine, address: int):
        if vm.accumulator < 0: 
            vm.cpu.set_program_location(address)


