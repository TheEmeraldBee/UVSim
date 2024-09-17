from src.instruction.instructions.load import LoadInstruction
from src.vm.virtual_machine import VirtualMachine


def test_add():
    vm = VirtualMachine()
    add_instruction = LoadInstruction()

    vm.get_memory().set(0, 69)
    add_instruction.handle(vm, 0)

    assert vm.accumulator == 69