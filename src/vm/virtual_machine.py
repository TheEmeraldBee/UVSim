from typing import Optional
from xml.etree.ElementTree import ParseError

from src.cpu.cpu import CPU
from src.instruction.event import InstructionEvent
from src.instruction.instructions.add import AddInstruction
from src.instruction.instructions.branch import BranchInstruction
from src.instruction.instructions.branch_neg import BranchNegInstruction
from src.instruction.instructions.branch_zero import BranchZeroInstruction
from src.instruction.instructions.division import DivisionInstruction
from src.instruction.instructions.halt import HaltInstruction
from src.instruction.instructions.multiply import MultiplyInstruction
from src.instruction.instructions.read import ReadInstruction
from src.instruction.instructions.subtract import SubtractInstruction
from src.instruction.instructions.write import WriteInstruction
from src.instruction.parsed_instruction import ParsedInstruction
from src.memory.memory import Memory

class VirtualMachine:
    def __init__(self):
        self._memory = Memory()
        self.accumulator = 0
        self.cpu = CPU([
            ReadInstruction(),
            WriteInstruction(),

            AddInstruction(),
            SubtractInstruction(),
            MultiplyInstruction(),
            DivisionInstruction(),

            BranchInstruction(),
            BranchZeroInstruction(),
            BranchNegInstruction(),

            HaltInstruction(),
        ])

    def handle(self, instruction: int) -> Optional[InstructionEvent]:
        if instruction == -99999:
            return InstructionEvent.EOF
        parsed = VirtualMachine.parse(instruction)

        instruction = self.cpu.get_instruction(parsed.instruction)
        if instruction is None:
            raise ValueError(f"Instruction {parsed.instruction} is not valid")

        return instruction.handle(self, parsed.address)

    def step(self) -> bool:
        instruction = self._memory.get(self.cpu.get_counter())
        event = self.handle(instruction)
        match event:
            case InstructionEvent.QUIT | InstructionEvent.EOF:
                self.cpu.advance_counter()
                return False
            case _:
                self.cpu.advance_counter()
                return True

    def get_memory(self) -> Memory:
        return self._memory

    @staticmethod
    def parse(number: int) -> ParsedInstruction:
        text = str(number)

        if number > 0:
            text = "+" + text

        if len(text) != 5:
            raise ParseError(f"Instruction length should be 5 characters, but found {len(text)}")

        sign_chr: chr = text[0]

        if sign_chr == '+':
            sign_num = 1
        elif sign_chr == '-':
            sign_num = -1
        else:
            raise ParseError(f"Unrecognized sign character `{sign_chr}`. Should be `+` or `-`")

        try:
            instruction = int(text[1:3])
        except ValueError:
            raise ParseError(f"Unrecognized number `{text[0:2]}`. Should be an integer")

        try:
            address = int(text[3:5])
        except ValueError:
            raise ParseError(f"Unrecognized number `{text[1:3]}`. Should be an integer")

        return ParsedInstruction(sign_num, instruction, address)
