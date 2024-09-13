from src.cpu.cpu import CPU
from src.vm.virtual_machine import VirtualMachine

class Main:
    """Main Class for the program"""

    def __init__(self):
        """Create Program Data Here"""
        self.vm = VirtualMachine(CPU())

    def run(self):
        """Run Program Here"""
        ...

if __name__ == "__main__":
    Main().run()
