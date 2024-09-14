from src.instruction.instruction import Instruction

class BranchNegInstruction(Instruction):
    instruction = 41

    def __init__(self):
        pass

    def handle(self, vm, address):
        if vm.accumulator < 0: 
            vm.cpu.set_program_location(address)


