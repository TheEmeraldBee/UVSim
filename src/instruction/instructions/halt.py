from src.instruction.event import InstructionEvent
from src.instruction.instruction import Instruction

class HaltInstruction(Instruction):
    instruction = 43

    def __init__(self):
        pass

    def handle(self, vm, address):
        return InstructionEvent.QUIT