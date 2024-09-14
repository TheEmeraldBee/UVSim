from enum import Enum

class InstructionEvent(Enum):
    QUIT = 1
    EOF = 2

    def __repr__(self):
        match self:
            case 1:
                return "Quit"
            case 2:
                return "End Of File"
            case _:
                return ""