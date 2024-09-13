import pytest

from instruction.instructions.division import DivisionInstruction
from src.memory.memory import Memory
from vm.virtual_machine import VirtualMachine


def test_division():
    vm = VirtualMachine()
    division_instruction = DivisionInstruction()

    vm.accumulator = 69
    
    vm.get_memory().set(0, 69)
    division_instruction.handle(vm, 0)
    
    assert vm.accumulator == 1