from logic_utils import check_guess
from streamlit.testing.v1 import AppTest

def test_new_game_button_resets_status_after_win():
    at = AppTest.from_file("app.py").run()
    at.session_state["status"] = "won"
    at.button[1].click().run()  # "New Game 🔁" is the second button (index 1)
    assert at.session_state["status"] == "playing"

def test_new_game_button_resets_status_after_loss():
    at = AppTest.from_file("app.py").run()
    at.session_state["status"] = "lost"
    at.button[1].click().run()
    assert at.session_state["status"] == "playing"

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"
