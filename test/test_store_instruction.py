from src.instruction.instructions.store import StoreInstruction
from src.vm.virtual_machine import VirtualMachine


def test_add():
    vm = VirtualMachine()
    add_instruction = StoreInstruction()

    vm.accumulator = 10 
    add_instruction.handle(vm, 0)

    vm.get_memory().get(0) == 10