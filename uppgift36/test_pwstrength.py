from uppgift36.pwstrength import compute_strength


def test_password_with_length_11_gives_1_point2():
    pw = "1" * 11
    assert compute_strength(pw) == 1


def test_password_with_length_5_gives_0_points2():
    pw = "1" * 5
    assert compute_strength(pw) == 0

def test_password_with_length_11_gives_1_point():
    pw = "1" * 11
    assert compute_strength(pw) == 1


def test_password_with_length_5_gives_0_points():
    pw = "1" * 5
    assert compute_strength(pw) == 50
