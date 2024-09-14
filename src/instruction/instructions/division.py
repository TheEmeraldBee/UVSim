from src.instruction.instruction import Instruction

class DivisionInstruction(Instruction):
    instruction = 32

    def __init__(self):
        pass

    def handle(self, vm, address):
        vm.accumulator = vm.accumulator // vm.get_memory().get(address)