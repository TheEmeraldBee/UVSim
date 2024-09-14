import getch

from src.instruction.instruction import Instruction

class ReadInstruction(Instruction):
    instruction = 10

    def __init__(self):
        pass

    def handle(self, vm, address):
        vm.get_memory().set(address, ord(getch.getch()))