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

- The game is a Streamlit-based number guessing game where the player selects a difficulty, enters guesses, receives Higher/Lower hints, and earns points for correct guesses.
- During testing, I found several bugs. The difficulty ranges were incorrect, the Higher/Lower hints were backwards, and guesses outside the allowed range could be accepted. I also found a game-state issue involving starting a new game after the previous game ended. The Developer Debug Info also exposed the secret number, which is useful for debugging but not for making the user experience actually a challenge.
- I fixed the game by correcting the difficulty ranges, validating guesses against the selected range, correcting the Higher/Lower messages, and making sure the game state resets correctly when starting a new game. I also refactored the core game functions into logic_utils.py and updated app.py to import and use those functions.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Open the Streamlit app and select a difficulty. The sidebar displays the correct range and number of attempts available.
2. Enter an invalid guess such as a number below the minimum or above the maximum. The game rejects the guess and displays an out-of-range message.
3. Enter a valid guess. If the guess is higher than the secret number, the game displays "Go LOWER!". If it is lower, the game displays "Go HIGHER!".
4. Continue making guesses until the secret number is found or the attempt limit is reached. The game displays the appropriate result without crashing.
5. Click New Game after finishing a game. The attempts, score, history, and game status reset so a new game can be played.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
$ pytest
============================= test session starts =============================
collected 5 items

tests/test_game_logic.py .....                                             [100%]

============================== 5 passed in 0.03s ==============================

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
