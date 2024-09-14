from src.cpu.cpu import CPU
from src.instruction.instructions.write import WriteInstruction


def test_cpu():
    cpu = CPU([WriteInstruction])

    assert len(cpu._instructions) == 1

    cpu.set_program_location(99)
    assert cpu._program_location == 99