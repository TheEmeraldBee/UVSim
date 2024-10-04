from typing import Optional, List

from src.instruction.instruction import Instruction


class CPU:
    """Class that represents a CPU that executes a set of instructions."""
    def __init__(self, instructions: List[Instruction]):
        """Initializes the CPU with a list of instructions."""
        self._instructions = instructions
        self._program_location = 0

    def get_counter(self):
        """Returns the current program counter location."""
        return self._program_location

    def advance_counter(self):
        """Advances the counter program by 1, making sure it does not exceed 99."""
        self._program_location += 1
        self._program_location = min(99, self._program_location)

    def with_instruction(self, instruction: Instruction):
        """Registers an instruction, returning self for method chaining."""
        self._instructions.append(instruction)
        return self

    def get_instruction(self, instr: int) -> Optional[Instruction]:
        """Retrieves an instruction from the CPU's instruction set based on the instruction code."""
        for instruction in self._instructions:
            if instruction.instruction == instr:
                return instruction
        return None

    def set_program_location(self, program_location: int):
        """Moves the program location to the given position."""
        if program_location >= 100 or program_location < 0:
            raise IndexError("desired program location out of program range.")
        self._program_location = program_location
