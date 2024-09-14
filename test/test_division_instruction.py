from src.instruction.instructions.division import DivisionInstruction
from src.vm.virtual_machine import VirtualMachine


def test_division():
    vm = VirtualMachine()
    division_instruction = DivisionInstruction()

    vm.accumulator = 69
    
    vm.get_memory().set(0, 69)
    division_instruction.handle(vm, 0)
    
    assert vm.accumulator == 1