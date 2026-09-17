# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
- The game looked normal the first time I ran it, and I was able to interact with it without an immediate crash or obvious error. Once I started testing different guesses and difficulty levels, I noticed that some of the game logic was not working as expected. The problems became more noticeable when I entered values outside of the expected range and when I switched to Hard mode.

- I noticed several bugs while testing the game. The hints could be backwards, such as the game telling me to go higher when my guess was already higher than the secret number, and sometimes the game could give inconsistent hints during different guesses. I also found that the game accepted numbers outside of the given range, including negative numbers. Another issue was the New Game button could stop working after the game ended because the previous game status was still being checked.


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

Bug Reproduction Log
Bug 1: Backwards hints
- Input : I entered a guess that was higher than the secret number.
- Expected Behavior: The game should tell me to go LOWER.
- Actual Behavior: The game told me to go HIGHER.
- Error / Output: The game displayed "📈 Go HIGHER!" even though my guess was higher than the secret.

Bug 2: Out-of-range guesses
- Input: I entered a number outside of the difficulty range, including -5 and numbers above the maximum.
- Expected Behavior: The game should reject the guess and tell me to enter a number within the allowed range.
- Actual Behavior: The game accepted the out-of-range number as a valid guess.
- Error / Output: No crash occurred, but the invalid number was processed as a guess.

Bug 3: New Game state
- Input : I clicked the New Game button after the game had ended.
- Expected Behavior: The game should reset the attempts, score, history, and status and start a fresh game.
- Actual Behavior: The previous game state could remain set to "lost," which prevented the new game from starting normally.
-Error / Output: The app displayed the game-over message instead of letting me continue with a fresh game.

Bug 4: Difficulty range
- Input: I switched between Normal and Hard difficulty.
- Expected Behavior: Normal should have a range of 1–50 and Hard should have a range of 1–100.
- Actual Behavior: The difficulty ranges were incorrect in the version I originally tested.
- Error / Output: The sidebar displayed the wrong maximum value for the affected difficulty.



---

## 2. How did you use AI as a teammate?

- I used Claude as my AI coding assistant to help me investigate the bugs in app.py and logic_utils.py. I asked it to look through the relevant files and explain where the problems were located before making changes. I also used the AI to help me understand why certain bugs were happening instead of just asking it to automatically fix everything.

-  One correct suggestion was that the range-validation problem was located in parse_guess() because the function accepted any integer without checking whether it was inside the current difficulty's range. The AI suggested passing the low and high values into parse_guess() and rejecting values outside those bounds. I verified the fix by testing values such as -5, 0, 101, 75 in different ranges, and valid values such as 1 and 50. The test showed that out-of-range values were rejected while valid values were accepted.

- One misleading part of the AI's analysis was when it initially described the Normal and Hard ranges as being reversed. I had already changed the ranges so that Normal was 1–50 and Hard was 1–100, so that explanation was based on an older version of my code. I checked the actual code and saw that the ranges were already set the way I intended, so I did not accept that suggestion as written. This taught me that I should always compare an AI's explanation with the current version of my code instead of assuming its analysis is automatically correct.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I decided a bug was fixed when I could reproduce the original problem and then confirm that the same input produced the expected behavior after the change. I did not just rely on the code looking correct because some of the bugs involved multiple pieces of Streamlit state. I also checked that the application still ran and that the changes did not create a new error.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
  One test I ran was for parse_guess(), where I tested negative numbers, zero, numbers at the boundaries, numbers above the maximum, and invalid text. For example, -5 and 101 were rejected for a 1–100 range, while 1 and 100 were accepted. I also tested 75 against a 1–50 range and confirmed that it was rejected. After updating my tests, I ran pytest and all 5 tests passed.
- Did AI help you design or understand any tests? How?
  Yes, AI helped me identify specific edge cases that should be tested instead of only testing normal guesses. It suggested checking values below the minimum, above the maximum, exactly at the boundaries, and invalid inputs such as letters or blank spaces. I then used those cases to verify that the new range validation worked correctly.

---

## 4. What did you learn about Streamlit and state?
- I learned that Streamlit reruns the Python script when the user interacts with the application, so the program needs to store information that should survive those reruns in st.session_state. I learned this especially through the New Game bug because clicking the button caused a rerun, but the game's status was still set to "lost", so the application could immediately stop again. Resetting values such as status, attempts, score, and history allowed the New Game button to actually create a fresh game.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- I would explain a Streamlit rerun as the app starting its Python script again whenever the user interacts with something on the page, such as clicking a button or entering an input. Because the script reruns, variables that are not saved can reset or lose their previous values. st.session_state acts like a storage space that keeps important game information, such as the secret number, score, attempts, and game status, between reruns. This is why session state is important for keeping the game from restarting or losing its information every time the user interacts with it.


## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - One habit I want to reuse is testing the specific edge cases that caused the bug instead of only checking that the program runs. I also want to get better at using Git commits throughout a project instead of waiting until everything is finished. Having separate commits for documenting bugs, fixing the code, and finishing the documentation makes it easier to track what changed and why.
- What is one thing you would do differently next time you work with AI on a coding task?
  Next time, I would give the AI more specific instructions and check the current code before accepting its explanation. I would also test each change immediately after making it instead of making several changes before checking the result. This would make it easier to identify which change caused a problem if something stopped working.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  This project showed me that AI-generated code can be helpful for finding patterns and explaining bugs, but it can also misunderstand the current state of a project. I learned that I should treat AI like a teammate whose suggestions I review and test, rather than someone whose code I automatically trust.
