from src.instruction.instruction import Instruction

class LoadInstruction(Instruction):
    instruction = 20

    def __init__(self):
        pass

    def handle(self, vm, address):
        vm.accumulator = vm.get_memory().get(address)