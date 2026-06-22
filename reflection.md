# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the game, the UI loaded correctly and appeared functional at first glance. However, once I started playing, I quickly noticed the hints were completely backwards - when I guessed too high, the game told me to "Go HIGHER!" which sent me in the wrong direction. I also noticed that the difficulty selector was misleading: choosing "Easy" still displayed "Guess a number between 1 and 100" even though the actual range was 1-20. Additionally, the scoring system awarded fewer points than expected when winning, making the game feel unfair.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input                    | Expected Behavior                         | Actual Behavior                            | Console Output / Error |
| ------------------------ | ----------------------------------------- | ------------------------------------------ | ---------------------- |
| Guess 75 (secret is 50)  | Hint says "📉 Go LOWER!"                  | Hint says "📈 Go HIGHER!"                  | none                   |
| Select "Easy" difficulty | UI says "Guess a number between 1 and 20" | UI says "Guess a number between 1 and 100" | none                   |
| Win on first attempt     | Score = 90 points (100 - 10×1)            | Score = 80 points (100 - 10×2)             | none                   |


---

## 2. How did you use AI as a teammate?

I used **Cursor AI (Claude)** as my primary AI tool for this project. I asked it to help me identify bugs in the codebase and understand what was going wrong with the game logic.

**Correct AI suggestion:** The AI correctly identified that the `check_guess` function in `app.py` had inverted hint messages - when `guess > secret`, the code returned "Go HIGHER!" instead of "Go LOWER!". I verified this by looking at lines 37-40 in the code and testing manually: when I guessed 75 and the secret was 50, the game incorrectly told me to go higher.

**Incorrect/Misleading AI suggestion:** While AI suggestions were generally helpful, one limitation was that AI couldn't actually run the game to verify its findings. It analyzed code statically but couldn't confirm real runtime behavior. I had to manually test each bug by playing the game myself to verify the issues were real and reproducible, rather than just trusting the AI's code analysis.

---

## 3. Debugging and testing your fixes

I decided a bug was fixed by running both automated tests and manual testing in the live game. After each fix, I ran `pytest tests/ -v` to ensure all unit tests passed, then played the game to confirm the fix worked in practice.

**Test I ran:** I asked AI to generate pytest cases targeting the specific bugs. For example, `test_too_high_hint_says_lower()` checks that when guess=75 and secret=50, the hint message contains "LOWER". Running pytest showed all 7 tests passed, confirming the logic was correct.

**AI's role in testing:** AI generated the test cases in `test_game_logic.py` based on the bugs we identified. It also noticed the original tests were broken (they expected a string but the function returns a tuple), and helped fix them to properly unpack `(outcome, message)`. This taught me that tests need to match the actual function signatures.

---

## 4. What did you learn about Streamlit and state?

Streamlit works by re-running your entire Python script from top to bottom every time the user interacts with the app (clicks a button, types in a text box, etc.). This means any regular variables you define get reset to their initial values on every interaction. To keep data persistent across these reruns, you use `st.session_state`, which is like a dictionary that survives the script re-execution. For example, `st.session_state.secret` stores the secret number so it doesn't change every time you submit a guess. Without session state, the game would be impossible to win because the answer would keep changing!

---

## 5. Looking ahead: your developer habits

**Habit to reuse:** I want to continue using the practice of writing pytest cases for bugs before and after fixing them. This "test-driven verification" approach gave me confidence that my fixes actually worked, and the tests serve as documentation for future developers.

**What I'd do differently:** Next time, I would make smaller, more frequent commits as I work through each phase, rather than doing all the work and then splitting commits at the end. This creates a more authentic git history.

**How this changed my thinking:** This project showed me that AI-generated code can look correct but contain subtle logic errors that only become apparent through testing. AI is a powerful starting point, but human review and verification are essential - I need to be the quality control, not just accept what AI produces.

