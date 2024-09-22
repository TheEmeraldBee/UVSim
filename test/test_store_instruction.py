from src.instruction.instructions.store import StoreInstruction
from src.vm.virtual_machine import VirtualMachine


def test_store():
    vm = VirtualMachine()
    add_instruction = StoreInstruction()

    vm.accumulator = 10
    add_instruction.handle(vm, 0)

    assert vm.get_memory().get(0) == 10


def test_store_negative():
    vm = VirtualMachine()
    add_instruction = StoreInstruction()

    vm.accumulator = -99
    add_instruction.handle(vm, 0)

    assert vm.get_memory().get(0) == -99
