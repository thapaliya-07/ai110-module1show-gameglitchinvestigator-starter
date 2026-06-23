from logic_utils import check_guess, update_score

def test_too_high():
    outcome, message = check_guess(100, 3)
    assert outcome == "Too High"

def test_too_low():
    outcome, message = check_guess(1, 50)
    assert outcome == "Too Low"

def test_correct_guess():
    outcome, message = check_guess(42, 42)
    assert outcome == "Win"

def test_wrong_guess_loses_points():
    new_score = update_score(50, "Too High", 1)
    assert new_score == 45
