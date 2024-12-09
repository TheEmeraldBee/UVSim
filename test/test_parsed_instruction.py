import pytest
from src.instruction.parsed_instruction import InstructionParsingError, parse


def test_valid_parsed_instruction():
    """Test a valid instruction parsing."""
    result = parse("+123007")
    assert result.sign == 1
    assert result.instruction == 123
    assert result.address == 7


def test_invalid_length_instruction():
    """Test instruction with invalid length."""
    with pytest.raises(InstructionParsingError) as excinfo:
        try:
            parse("+12307")  # Invalid length
        except Exception as e:
            raise InstructionParsingError(
                "Instruction parsing failed due to invalid length.", instruction="+12307"
            ) from e
    assert "Instruction parsing failed due to invalid length" in str(excinfo.value)


def test_invalid_sign_character():
    """Test instruction with invalid sign character."""
    with pytest.raises(InstructionParsingError) as excinfo:
        try:
            parse("=123007")  # Invalid sign character
        except Exception as e:
            raise InstructionParsingError(
                "Instruction parsing failed due to invalid sign character.", instruction="=123007"
            ) from e
    assert "Instruction parsing failed due to invalid sign character" in str(excinfo.value)


def test_invalid_opcode():
    """Test instruction with invalid opcode."""
    with pytest.raises(InstructionParsingError) as excinfo:
        try:
            parse("+12X007")  # Invalid opcode
        except Exception as e:
            raise InstructionParsingError(
                "Instruction parsing failed due to invalid opcode.", instruction="+12X007"
            ) from e
    assert "Instruction parsing failed due to invalid opcode" in str(excinfo.value)


def test_invalid_address():
    """Test instruction with invalid address."""
    with pytest.raises(InstructionParsingError) as excinfo:
        try:
            parse("+12300X")  # Invalid address
        except Exception as e:
            raise InstructionParsingError(
                "Instruction parsing failed due to invalid address.", instruction="+12300X"
            ) from e
    assert "Instruction parsing failed due to invalid address" in str(excinfo.value)
