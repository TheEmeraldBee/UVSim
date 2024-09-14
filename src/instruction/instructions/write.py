from src.instruction.instruction import Instruction

class WriteInstruction(Instruction):
    instruction = 11

    def __init__(self):
        pass

    def handle(self, vm, address):
        print(chr(vm.get_memory().get(address)))