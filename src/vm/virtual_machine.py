from typing import Optional, TYPE_CHECKING

from src.cpu.cpu import CPU
from src.instruction.event import InstructionEvent
from src.instruction.instructions.add import AddInstruction
from src.instruction.instructions.branch import BranchInstruction
from src.instruction.instructions.branch_neg import BranchNegInstruction
from src.instruction.instructions.branch_zero import BranchZeroInstruction
from src.instruction.instructions.division import DivisionInstruction
from src.instruction.instructions.halt import HaltInstruction
from src.instruction.instructions.load import LoadInstruction
from src.instruction.instructions.multiply import MultiplyInstruction
from src.instruction.instructions.read import ReadInstruction
from src.instruction.instructions.store import StoreInstruction
from src.instruction.instructions.subtract import SubtractInstruction
from src.instruction.instructions.write import WriteInstruction
from src.instruction.parsed_instruction import parse
from src.memory.memory import Memory


class VirtualMachine:
    """Class that represents a virtual machine which executes instructions using a CPU and memory."""

    def __init__(self):
        """Initializes the virtual machine with a memory unit, an accumulator set to 0, and a CPU initialized with a set of standard instructions."""
        self._memory = Memory()
        self.accumulator = 0
        self.cpu = CPU(
            [
                ReadInstruction(),
                WriteInstruction(),
                AddInstruction(),
                SubtractInstruction(),
                MultiplyInstruction(),
                DivisionInstruction(),
                LoadInstruction(),
                StoreInstruction(),
                BranchInstruction(),
                BranchZeroInstruction(),
                BranchNegInstruction(),
                HaltInstruction(),
            ]
        )

    # Handles executing an instruction while checking for EOF.
    def handle(self, instruction: int, output) -> Optional[InstructionEvent]:
        """Handles the execution of an instruction and checks for special cases such as EOF."""
        if instruction == -99999:
            return InstructionEvent.EOF

        # Breaks the instruction into its respective sign, opcode, and address.
        parsed = parse(instruction)
        if parsed is None:
            return None

        instr = self.cpu.get_instruction(parsed.instruction)
        if instr is None:
            raise ValueError(f"Instruction {parsed.instruction} is not valid")
        return instr.handle(self, parsed.address, output)

    # Handles one instruction, executes, updates counter.
    def step(self, output) -> bool:
        instruction = self._memory.get(self.cpu.get_counter())
        event = self.handle(instruction, output)

        match event:
            case InstructionEvent.QUIT | InstructionEvent.EOF:
                self.cpu.advance_counter()
                return False
            case _:
                self.cpu.advance_counter()
                return True

    def get_memory(self) -> Memory:
        """Returns the memory object of the virtual machine"""
        return self._memory
