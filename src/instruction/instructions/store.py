from src.instruction.instruction import Instruction

class StoreInstruction(Instruction):
    instruction = 21

    def __init__(self):
        pass

    def handle(self, vm, address):
        vm.get_memory().set(address, vm.accumulator)