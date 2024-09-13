from src.instruction.instruction import Instruction


class CPU:
    def __init__(self):
        self._program_location = 0
        self._instructions: [Instruction] = []

    def with_instruction(self, instruction: Instruction):
        self._instructions.append(instruction)
        return self

    def set_program_location(self, program_location: int):
        self._program_location = program_location