from src.memory.memory import Memory

class VirtualMachine:
    def __init__(self):
        self._memory = Memory()
        self.accumulator = 0

    def get_memory(self) -> Memory:
        return self._memory