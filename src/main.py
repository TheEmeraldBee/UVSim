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

        # Ensure we have 1 argument (1 for the python file, and 1 for the filepath to run).
        if len(args) != 2:
            raise Exception(f"Expected 1 argument, found {len(args) - 1}")


        # Open the file from the passed filepath.
        path = args[1]
        with open(path, "r") as f:
            lines = f.readlines()
            for i in range(0, len(lines)):
                # Try to set the memory with the line, while catching errors parsing extructions.

                try:
                    self.vm.get_memory().set(i, int(lines[i]))
                except ValueError:
                    raise Exception(f"Invalid File Code `{lines[i]}`, should be an integer.")
                
        # Step through the VM, handling each instruction in the program memory.
        while self.vm.step():
            ...

if __name__ == "__main__":
    Main().run()
