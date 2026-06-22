from logic_utils import check_guess, update_score, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_too_high_hint_says_lower():
    # BUG FIX TEST: When guess is too high, hint should say "LOWER" not "HIGHER"
    outcome, message = check_guess(75, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'LOWER' in hint but got: {message}"

def test_too_low_hint_says_higher():
    # BUG FIX TEST: When guess is too low, hint should say "HIGHER" not "LOWER"
    outcome, message = check_guess(25, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected 'HIGHER' in hint but got: {message}"

def test_score_first_attempt_win():
    # BUG FIX TEST: Win on attempt 1 should give 90 points (100 - 10*1)
    score = update_score(0, "Win", 1)
    assert score == 90, f"Expected 90 points for first attempt win, got {score}"

def test_easy_difficulty_range():
    # BUG FIX TEST: Easy mode should have range 1-20
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20
