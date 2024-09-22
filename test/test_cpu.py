import pytest

from src.cpu.cpu import CPU
from src.instruction.instructions.write import WriteInstruction


def test_cpu():
    cpu = CPU([WriteInstruction])

    assert len(cpu._instructions) == 1

    cpu.set_program_location(99)
    assert cpu._program_location == 99


def test_cpu_overcounter():
    cpu = CPU([WriteInstruction])

    cpu.set_program_location(99)

    # Try to advance past 99
    cpu.advance_counter()

    # Ensure it is still 99
    assert cpu._program_location == 99


def test_cpu_fail():
    cpu = CPU([WriteInstruction])

    with pytest.raises(IndexError):
        cpu.set_program_location(100)
