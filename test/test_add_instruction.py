import pytest

from instruction.instructions.add import AddInstruction
from src.memory.memory import Memory
from vm.virtual_machine import VirtualMachine


def test_add():
    vm = VirtualMachine()
    add_instruction = AddInstruction()

    vm.get_memory().set(0, 69)
    add_instruction.handle(vm, 0)

    assert vm.accumulator == 69