from src.instruction.instructions.branch import BranchInstruction
from src.instruction.instructions.branch_neg import BranchNegInstruction
from src.instruction.instructions.branch_zero import BranchZeroInstruction
from src.vm.virtual_machine import VirtualMachine


def test_branch():
    vm = VirtualMachine()

    instruction = BranchInstruction()

    instruction.handle(vm, 65)
    assert vm.cpu._program_location == 65


def test_branch_neg_success():
    vm = VirtualMachine()
    instruction = BranchNegInstruction()

    vm.accumulator = -1
    instruction.handle(vm, 65)

    assert vm.cpu._program_location == 65


def test_branch_neg_fail():
    vm = VirtualMachine()
    instruction = BranchNegInstruction()

    vm.accumulator = 0
    instruction.handle(vm, 90)

    assert vm.cpu._program_location == 0


def test_branch_zero_success():
    vm = VirtualMachine()
    instruction = BranchZeroInstruction()

    vm.accumulator = 0
    instruction.handle(vm, 65)

    assert vm.cpu._program_location == 65


def test_branch_zero_fail():
    vm = VirtualMachine()
    instruction = BranchZeroInstruction()

    vm.accumulator = 1
    instruction.handle(vm, 90)

    assert vm.cpu._program_location == 0
