from src.instruction.instruction import Instruction

class SubtractInstruction(Instruction):
    instruction = 31

    def __init__(self):
        pass

    def handle(self, vm, address):
        vm.accumulator -= vm.get_memory().get(address)
