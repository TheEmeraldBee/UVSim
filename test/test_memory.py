import pytest

from src.memory.memory import Memory


def test_memory():
    memory = Memory()

    # Assert that memory is correctly set.
    memory.set(0, 10)
    assert memory.get(0) == 10

    # Assert memory length is correct.
    assert len(memory._memory) == 100

    # Assert that accessing out of memory ranges raises an index error.
    with pytest.raises(IndexError): (
        memory.get(-1),
        memory.set(-1, 0)
    )

    with pytest.raises(IndexError): (
        memory.get(100),
        memory.set(100, 0)
    )