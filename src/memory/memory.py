class Memory:
    def __init__(self):
        self._memory = [0 for _ in range(0, 100)]

    def set(self, address: int, value: int) -> None:
        if address >= len(self._memory) or address < 0:
            raise IndexError("Address out of memory range (0, 99)")
        self._memory[address] = value

    def get(self, address: int) -> int:
        if address >= len(self._memory) or address < 0:
            raise IndexError("Address out of memory range (0, 99)")
        return self._memory[address]