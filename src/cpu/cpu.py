from typing import Optional

from src.instruction.instruction import Instruction

class CPU:
    def __init__(self, instructions: [Instruction]):
        self._instructions = instructions
        self._program_location = 0

    def get_counter(self):
        return self._program_location

    def advance_counter(self):
        self._program_location += 1

    def with_instruction(self, instruction: Instruction):
        """Registers an instruction, returning self for method chaining."""
        self._instructions.append(instruction)
        return self

    def get_instruction(self, instr: int) -> Optional[Instruction]:
        for instruction in self._instructions:
            if instruction.instruction == instr:
                return instruction
        return None

    def set_program_location(self, program_location: int):
        """Moves the program location to the given position."""
        self._program_location = program_location