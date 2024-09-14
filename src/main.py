import sys

from src.vm.virtual_machine import VirtualMachine

class Main:
    """Main Class for the program"""

    def __init__(self):
        """Create Program Data Here"""
        self.vm = VirtualMachine()

    def run(self):
        """Run Program Here"""
        args = sys.argv
        if len(args) != 2:
            raise Exception(f"Expected 1 argument, found {len(args) - 1}")

        path = args[1]
        with open(path, "r") as f:
            lines = f.readlines()
            for i in range(0, len(lines)):
                try:
                    self.vm.get_memory().set(i, int(lines[i]))
                except ValueError:
                    raise Exception(f"Invalid File Code `{lines[i]}`, should be an integer.")
        while self.vm.step():
            ...

if __name__ == "__main__":
    Main().run()
