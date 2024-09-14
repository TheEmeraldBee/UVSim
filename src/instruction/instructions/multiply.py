from src.instruction.instruction import Instruction

class MultiplyInstruction(Instruction):
    instruction = 33

    def __init__(self):
        pass

    def handle(self, vm, address):
        vm.accumulator *= vm.get_memory().get(address)
