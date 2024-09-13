from src.instruction.instruction import Instruction

class CPU:
    def __init__(self):
        self._instructions = []
        self._program_location = 0

    def with_instruction(self, instruction: Instruction):
        """Registers an instruction, returning self for method chaining."""
        self._instructions.append(instruction)
        return self

    def set_program_location(self, program_location: int):
        """Moves the program location to the given position."""
        self._program_location = program_location