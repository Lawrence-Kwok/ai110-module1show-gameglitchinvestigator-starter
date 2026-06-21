# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

While running the game for the first time and playing through it through several iterations, several bugs were noted:

(1) The hints were the opposite of the direction that the player should be 
(2) After pressing "New Game" after a win or game over the game doesn't reset and doesn't respond to any new inputs
(3) When entering a number out of range, instead of saying the input is invalid or out of range, it alternates between
saying go Lower or go Higher

| Input Used  | Expected Behavior | Actual Behavior | Console Error / Output |
| :---------------- | :---- | :---- | :---- |
| guess of 1 on Normal| Correct or Go Higher| Go Lower | None |
| guess of 100 on Normal| Correct or Go Lower| Go Higher | None |
| guess of 400 on Normal| Out of Range / Invalid | Go Higher / Go Lower | None | 
| Pressing New Game After Win or Game Over | Reset | Game Over Message or You Won Message Persists| None |

Input Used | Expected Behavior | Actual Behavior | Console Error / Output
-------------------------------------------------------------------------

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

In this case I used the Claude plugin for VSCode, which 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

Creating templates or reusable patterns are important for increasing the speed and efficiency of the 

AI in its current state is getting more expensive with the subsidies or loss leaders (Github Co-Pilot, etc) running out, so being able to accurately describe and give enough limited context to ensure that your requests are focused and small enough that its easier to verify and prevent drift early. I think of it as a very powerful tool for prototyping and mocking up proof of concepts which can be good for proving whether an idea is feasible or not, but it comes with the understanding that you have to verify the results whether it is through robust test cases and/or workflows. 