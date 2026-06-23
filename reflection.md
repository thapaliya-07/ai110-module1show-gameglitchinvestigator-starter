# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  When I first ran the game, I noticed three bugs:

1. **Hints were backwards** — I guessed 100 when the secret was 3, and the game told me to go even higher instead of lower.

2. **Score rewarded wrong guesses** — On certain attempts, 
   guessing incorrectly actually added +5 points to my score 
   instead of penalizing me.

3. **Hard difficulty is easier than Normal** — Hard mode only 
   uses range 1–50, which is a smaller range than Normal (1–100), making it accidentally easier.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess of 100, secret was 3 | "Too High / Go Lower" hint | "Go HIGHER!" shown | none |
| Any wrong guess on even-numbered attempt | Score stays same or drops | Score increases by +5 | none |
| Switching difficulty to Hard | Harder/wider number range | Range 1–50 (narrower than Normal) | none
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

**Correct AI suggestion:**
I asked the AI to explain why the hints were backwards. It correctly
identified that the secret number was being converted to a string on
even-numbered attempts, causing text comparison instead of number
comparison. I verified this by reading the buggy code in app.py and
confirming the `str()` conversion was there. The fix worked — hints
are now correct.

**Incorrect/misleading AI suggestion:**
The AI initially suggested keeping all the logic inside app.py instead
of moving it to logic_utils.py. This was misleading because the project
requires separation of logic and UI code. I rejected this and instead
moved all four functions into logic_utils.py manually, then imported
them into app.py.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I verified my fixes in two ways:

1. **Manual testing** — I ran the game with `python3 -m streamlit run
app.py` and tested guesses above and below the secret number. The hints
now correctly say "Go LOWER" when guessing too high and "Go HIGHER"
when guessing too low.

2. **Automated testing** — I wrote four pytest cases in
`tests/test_game_logic.py` covering too high, too low, correct guess,
and score deduction. All 4 tests passed when running `python3 -m pytest
tests/`.

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
