from src.instruction.instruction import Instruction

class BranchInstruction(Instruction):
    instruction = 40

    def __init__(self):
        pass

    def handle(self, vm, address):
        vm.cpu.set_program_location(address)

