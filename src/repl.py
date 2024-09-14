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
                    for i in range(0, 100):
                        print(f" - {i} = {self.vm.get_memory().get(i)}")

                    print("-" * 10)

                    continue
                case 'accumulator':
                    print(f"\nProgram Accumulator is currently: {self.vm.accumulator}")
                    continue
                case 'quit':
                    return
            try:
                result = self.vm.handle(int(text))
                print(f"Instruction returned: {result}")
            except ValueError as e:
                print(f"Instruction Errored: {e}")

if __name__ == "__main__":
    Main().run()
