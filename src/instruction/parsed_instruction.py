class ParsedInstruction:
    def __init__(self, sign: int, instruction: int, address: int):
        self.sign = sign
        self.instruction = instruction
        self.address = address

    def __repr__(self):
        if self.sign == 1:
            sign_text = '+'
        else:
            sign_text = '-'

        return f"{sign_text} : {self.instruction} : {self.address}"