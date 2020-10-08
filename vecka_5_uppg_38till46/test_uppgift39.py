from vecka_5_uppg_38till46.uppgift39 import maximum


def test_a_is_max():
    assert maximum(5, 4, 3) == 5


def test_b_is_max():
    assert maximum(5, 54, 3) == 54


def test_c_is_max():
    assert maximum(5, 54, 300) == 300
