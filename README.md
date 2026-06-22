# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Game's purpose:** A number guessing game where players try to guess a secret number within a limited number of attempts, receiving "higher" or "lower" hints after each guess.

- [x] **Bugs found:**
  1. Inverted hints - "Go HIGHER" shown when guess was too high (should say "Go LOWER")
  2. Hardcoded range display - UI always showed "1 to 100" regardless of difficulty setting
  3. Scoring formula bug - used `attempt_number + 1` causing 10-point deficit
  4. New Game button didn't reset game status, preventing replay after winning
  5. Double-click required to submit, Enter key didn't work

- [x] **Fixes applied:**
  1. Corrected hint messages in `check_guess()` function in `logic_utils.py`
  2. Changed hardcoded "1 and 100" to use `{low}` and `{high}` variables
  3. Fixed scoring formula to use `attempt_number` instead of `attempt_number + 1`
  4. Added `st.session_state.status = "playing"` reset in New Game handler
  5. Wrapped input in `st.form()` to enable Enter key and single-click submit

## 📸 Demo Walkthrough

1. User selects "Easy" difficulty from the sidebar - UI correctly displays "Guess a number between 1 and 20"
2. User enters a guess of 15 and presses Enter (or clicks Submit) - form submits on first action
3. Game shows "📉 Go LOWER!" hint, indicating the secret is less than 15
4. User enters a guess of 7 - Game shows "📈 Go HIGHER!" hint
5. User enters a guess of 10 - Game shows "📉 Go LOWER!"
6. User enters a guess of 9 - "🎉 Correct!" message appears with balloons
7. Score displays correctly (e.g., 60 points for winning on attempt 4: 100 - 10×4)
8. User clicks "New Game" - game resets properly and allows a new round

## 🧪 Test Results

```
============================= test session starts =============================
platform win32 -- Python 3.12.7, pytest-7.4.4, pluggy-1.0.0
rootdir: C:\Users\wurub\OneDrive\Desktop\codepath\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.2.0
collected 7 items

tests/test_game_logic.py::test_winning_guess PASSED                      [ 14%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 28%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 42%]
tests/test_game_logic.py::test_too_high_hint_says_lower PASSED           [ 57%]
tests/test_game_logic.py::test_too_low_hint_says_higher PASSED           [ 71%]
tests/test_game_logic.py::test_score_first_attempt_win PASSED            [ 85%]
tests/test_game_logic.py::test_easy_difficulty_range PASSED              [100%]

============================== 7 passed in 0.02s ==============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
