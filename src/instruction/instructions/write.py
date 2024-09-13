from src.instruction.instruction import Instruction
from src.vm.virtual_machine import VirtualMachine


class WriteInstruction(Instruction):
    instruction = 11

    def __init__(self):
        pass

    def handle(self, vm: VirtualMachine, address: int):
        print(chr(vm.get_memory().get(address)))