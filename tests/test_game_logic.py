from logic_utils import check_guess, parse_guess


def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_out_of_range_guess():
    ok, guess, error = parse_guess("101", 1, 100)
    assert ok is False
    assert guess is None
    assert "Out of range" in error


def test_valid_boundary_guess():
    ok, guess, error = parse_guess("1", 1, 100)
    assert ok is True
    assert guess == 1
    assert error is None