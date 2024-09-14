from src.cpu.cpu import CPU
from src.instruction.instructions.branch import BranchInstruction
from src.instruction.instructions.branch_neg import BranchNegInstruction
from src.instruction.instructions.branch_zero import BranchZeroInstruction
from src.instruction.instructions.write import WriteInstruction
from src.vm.virtual_machine import VirtualMachine

def test_branch():
    vm = VirtualMachine()

    instruction = BranchInstruction()

    instruction.handle(vm, 65)
    assert vm.cpu._program_location == 65

def test_branch_neg():
    vm = VirtualMachine()

    instruction = BranchNegInstruction()

    vm.accumulator = -1
    instruction.handle(vm, 65)

    assert vm.cpu._program_location == 65

    vm.accumulator = 0
    instruction.handle(vm, 90)
    
    assert vm.cpu._program_location == 65

def test_branch_zero():
    vm = VirtualMachine()

    instruction = BranchZeroInstruction()

    vm.accumulator = 0
    instruction.handle(vm, 65)

    assert vm.cpu._program_location == 65

    vm.accumulator = 1
    instruction.handle(vm, 90)
    
    assert vm.cpu._program_location == 65