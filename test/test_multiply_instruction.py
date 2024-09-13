import pytest

from instruction.instructions.multiply import MultiplyInstruction
from src.memory.memory import Memory
from vm.virtual_machine import VirtualMachine


def test_multiply():
    vm = VirtualMachine()
    multiply_instruction = MultiplyInstruction()

    vm.accumulator = 2
    
    vm.get_memory().set(0, 69)
    multiply_instruction.handle(vm, 0)
    
    assert vm.accumulator == 138