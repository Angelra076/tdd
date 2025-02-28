import pytest
from water_dispenser import WaterDispenser

@pytest.fixture
def dispenser():
    return WaterDispenser()

@pytest.mark.parametrize("mode, amount, expected", [
    ("fría", 2, "El agua no está suficientemente fría"),
    ("caliente", 2, "El agua no está suficientemente caliente"),
    ("ambiente", 2, "Dispensando 2 litros de agua ambiente")
])
def test_dispense(dispenser, mode, amount, expected):
    assert dispenser.dispense(mode, amount) == expected


def test_dispense_with_cold_temp(dispenser):
    dispenser.set_cold_temp(10)
    assert dispenser.dispense("fría", 2) == "Dispensando 2 litros de agua fría"


def test_dispense_with_hot_temp(dispenser):
    dispenser.set_hot_temp(90)
    assert dispenser.dispense("caliente", 2) == "Dispensando 2 litros de agua caliente"


def test_insufficient_water(dispenser):
    dispenser.current_level = 1
    assert dispenser.dispense("ambiente", 2) == "Agua insuficiente, reponer bidón"


def test_refill(dispenser):
    dispenser.current_level = 0
    assert dispenser.refill() == "Bidón de agua reemplazado"
    assert dispenser.current_level == dispenser.capacity
