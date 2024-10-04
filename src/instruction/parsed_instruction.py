from lib2to3.pgen2.parse import ParseError


class ParsedInstruction:
    def __init__(self, sign: int, instruction: int, address: int):
        self.sign = sign
        self.instruction = instruction
        self.address = address

    def __repr__(self):
        if self.sign == 1:
            sign_text = "+"
        else:
            sign_text = "-"

        return f"{sign_text} : {self.instruction} : {self.address}"


def parse(number: int) -> ParsedInstruction | None:
    if number == 0:
        return None

    text = str(number)

    # Handles the machine instruction while checking for the sign and opcode.
    if number > 0:
        text = "+" + text

    if len(text) != 5:
        raise ParseError(
            f"Instruction length should be 5 characters, but found {len(text)}"
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
        instruction = int(text[1:3])
    except ValueError:
        raise ParseError(f"Unrecognized number `{text[0:2]}`. Should be an integer")

    try:
        address = int(text[3:5])
    except ValueError:
        raise ParseError(f"Unrecognized number `{text[1:3]}`. Should be an integer")

    return ParsedInstruction(sign_num, instruction, address)
