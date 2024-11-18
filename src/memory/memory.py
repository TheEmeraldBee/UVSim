from src.cpu.cpu import CPU
import tkinter.messagebox as msg


class Memory:
    """Class that represents a memory storage for the virtual machine"""
    def __init__(self, memory_size):
        """Initializes the memory with the given number of addresses, each set to 0"""
        self._memory = [0 for _ in range(memory_size)]

    def set(self, address: int, value: int) -> None:
        """Sets the value in a specific memory address"""
        if address >= len(self._memory) or address < 0:
            raise IndexError(f"Address out of memory range (0, {len(self._memory) - 1})")
        self._memory[address] = value

    def get(self, address: int) -> int:
        """Retrieves the value from a specific memory address"""
        if address >= len(self._memory) or address < 0:
            raise IndexError(f"Address out of memory range (0, {len(self._memory) - 1})")
        return self._memory[address]

    def load_file(self, path) -> str:
        """Loads a file with instructions into the memory, starting at address 0. Each line in the file is an instruction"""
        with open(path, "r") as file:
            idx = 0

            for line in file:
                # Strip Whitespace and Ignore empty lines
                line = line.strip()
                if line == "":
                    continue

                # Remove + signs
                if line[0] == "+":
                    line = line[1::]
                try:
                    code = int(line)
                except ValueError:
                    
                    msg.showerror("Value Error","Please select a .txt file." )
                    raise ValueError(f"Invalid input for int. {line} should be an integer.")

                self.set(idx, code)
                idx += 1
