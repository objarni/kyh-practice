from vecka_5_uppg_38till46.uppgift39 import maximum, summa, produkt


def test_a_is_max():
    assert maximum(5, 4, 3) == 5


def test_b_is_max():
    assert maximum(5, 54, 3) == 54


def test_c_is_max():
    assert maximum(5, 54, 300) == 300


def test_summa_av_enkel_lista():
    assert summa([1, 2, 3]) == 6


def test_summa_av_tom_lista():
    assert summa([]) == 0


def test_summa_av_pos_neg_tal():
    assert summa([50, -50]) == 0

def test_produkt_av_enkel_lista():
    assert produkt([1, 2, 3, 4]) == 24


def test_produkt_av_tom_lista():
    assert produkt([]) == 1


def test_produkt_av_pos_neg_tal():
    assert produkt([5, -5]) == -25
