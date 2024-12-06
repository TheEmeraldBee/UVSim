from enum import Enum


class InstructionEvent(Enum):
    """Enum representing different instruction events"""
    QUIT = 1
    EOF = 2
    NO_ADVANCE = 3

    def __repr__(self) -> str:
        match self:
            case 1:
                return "Quit"
            case 2:
                return "End Of File"
            case 3:
                return "Don't Advance"
            case _:
                return ""
