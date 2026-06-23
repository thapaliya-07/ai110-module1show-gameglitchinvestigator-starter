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

**What bugs did you find?**
- Hints were backwards due to secret number being converted to a string
  on even attempts, causing text comparison instead of number comparison.
- Score rewarded wrong guesses with +5 points on even attempts.
- Hard difficulty had range 1–50, making it easier than Normal (1–100).

**How did you fix them?**
- Removed the string conversion so secret is always compared as an integer.
- Simplified update_score so wrong guesses always deduct 5 points.
- Changed Hard difficulty range to 1–200.
- Moved all logic functions into logic_utils.py and imported them in app.py.

**What did you learn?**
- AI-generated code can have subtle bugs that only show up when you
  actually play/test the app.
- Separating logic from UI code makes bugs easier to find and fix.
- Automated tests give you confidence that fixes actually work.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User selects difficulty "Normal" (range 1–100)
2. User enters a guess of 40 → Game returns "Go HIGHER" (too low)
3. User enters a guess of 70 → Game returns "Go LOWER" (too high)
4. User enters a guess of 55 → Game returns "Go LOWER" (too high)
5. User enters a guess of 48 → Game returns "Go HIGHER" (too low)
6. User enters a guess of 52 → "Correct!" — game ends
7. Score updates based on number of attempts taken
8. User clicks "New Game" to play again

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
