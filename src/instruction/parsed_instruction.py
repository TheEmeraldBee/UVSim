from lib2to3.pgen2.parse import ParseError
import tkinter.messagebox as msg

# The length of an instruction
INSTRUCTION_CODE_LENGTH = 3

# An instruction, and an address, + 1 for the sign!
INSTRUCTION_LENGTH = (INSTRUCTION_CODE_LENGTH * 2) + 1

class ParsedInstruction:
    """Represents a fully parsed instruction, making each piece of an instruction easier to understand."""
    def __init__(self, sign: int, instruction: int, address: int):
        self.sign = sign
        self.instruction = instruction
        self.address = address

    def __repr__(self) -> str:
        if self.sign == 1:
            sign_text = "+"
        else:
            sign_text = "-"

        return f"{sign_text} : {self.instruction} : {self.address}"


def parse(number: str) -> ParsedInstruction | None:
    """Parse an instruction, returning None if the value is 0, and raising an error if no instruction is valid."""
    if number == 0:
        return None
    
    text = str(number)

    # Handles the machine instruction while checking for the sign and opcode.
    if number > 0:
        text = "+" + text

    if len(text) == 6:
        text = text[0] + "0" + text[1::]

    if len(text) != INSTRUCTION_LENGTH:
        raise Exception(
            f"Instruction length should be {INSTRUCTION_LENGTH} characters, but found {len(text)}"
        )

    sign_chr: chr = text[0]

    if sign_chr == "+":
        sign_num = 1
    elif sign_chr == "-":
        sign_num = -1
    else:
        raise ParseError(
            f"Unrecognized sign character `{sign_chr}`. Should be `+` or `-`"
        )

    # Tries to extract the opcode and the address while catching errors.
    try:
        instruction = int(text[1:4:])
    except ValueError:
        msg.showerror("Value Error", f"Unrecognized number `{text[0:2]}`. Should be an integer")
        raise ParseError(f"Unrecognized number `{text[0:2]}`. Should be an integer")

    try:
        address = int(text[4::])
    except ValueError:
        msg.showerror("Value Error", f"Unrecognized number `{text[1:3]}`. Should be an integer")

        raise ParseError(f"Unrecognized number `{text[1:3]}`. Should be an integer")

    return ParsedInstruction(sign_num, instruction, address)
