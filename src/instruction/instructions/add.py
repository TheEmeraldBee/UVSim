from src.instruction.instruction import Instruction


class AddInstruction(Instruction):
    instruction = 30

    def __init__(self):
        pass

    def handle(self, vm, address):
        vm.accumulator += vm.get_memory().get(address)
