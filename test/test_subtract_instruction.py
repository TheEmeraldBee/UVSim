from src.instruction.instructions.subtract import SubtractInstruction
from src.vm.virtual_machine import VirtualMachine


def test_subtract():
    vm = VirtualMachine()
    subtract_instruction = SubtractInstruction()

    vm.get_memory().set(0, 69)
    subtract_instruction.handle(vm, 69)

    assert vm.accumulator == 0

def test_subtract_zero():
    vm = VirtualMachine()
    subtract_instruction = SubtractInstruction()

    vm.get_memory().set(0, 0)
    subtract_instruction.handle(vm, 0)

    assert vm.accumulator == 0