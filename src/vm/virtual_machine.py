from src.memory.memory import Memory

class VirtualMachine:
    def __init__(self, cpu):
        self._memory = Memory()
        self.accumulator = 0
        self.cpu = cpu

    def get_memory(self) -> Memory:
        return self._memory