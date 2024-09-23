from src.vm.virtual_machine import VirtualMachine

class Main:
    """Main Class for the program"""

    def __init__(self):
        """Create Program Data Here"""
        self.vm = VirtualMachine()

    def run(self):
        """Run Program Here"""
        while True:
            text = input(">>> ")
            match text:
                case 'memory':
                    print("\nProgram Memory: ")
                    # If 'memory' is entered in the program, all memory values (0 - 99) are printed in the vm.

                    for i in range(0, 100):
                        print(f" - {i} = {self.vm.get_memory().get(i)}")

                    print("-" * 10)

                    continue
                # If 'accumulator' is entered in the program, the current value of the acummulator is printed.

                case 'accumulator':
                    print(f"\nProgram Accumulator is currently: {self.vm.accumulator}")
                    continue
                case 'quit':
                    return
                
            # Tries to see if the input is a recognized command. If so, the instruction is printed. Otherwise an error is thrown.
            try:
                result = self.vm.handle(int(text))
                print(f"Instruction returned: {result}")
            except ValueError as e:
                print(f"Instruction Errored: {e}")

if __name__ == "__main__":
    Main().run()
