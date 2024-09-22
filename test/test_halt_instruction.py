from src.instruction.event import InstructionEvent
from src.instruction.instructions.halt import HaltInstruction
from src.vm.virtual_machine import VirtualMachine


def test_halt():
    vm = VirtualMachine()
    instruction = HaltInstruction()

    assert instruction.handle(vm, 0) == InstructionEvent.QUIT
