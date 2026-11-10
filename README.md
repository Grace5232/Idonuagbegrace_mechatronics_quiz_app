# Mechatronics Quiz App

## What it does
This is a multiple-choice quiz about mechatronics and basic electronics, written in Python. It covers topics such as resistors, Ohm's law, electrical current, relays, PLCs, sensors and servo motors. The 8 questions, their four options, the correct answers and the hints are all stored in lists.

When the program runs, it shuffles the questions so every attempt is in a different order. It shows each question with numbered options and the user types the number of their answer. The program checks the answer, tells the user straight away if they were right or wrong, and keeps a running score. At the end it shows the final score, a percentage and a grade message (from "Excellent!" for 80% and above to "Keep studying" for below 40%). If the user types a letter, or a number that is not one of the options, the program shows a friendly message and asks again instead of crashing.

## How to run it
Install Python 3, then run: python mechatronic_quiz_app.py

## Sample output
```
=== Mechatronics Quiz ===
Answer by typing the option number. Type h for a hint (costs half a mark).

Question 1 of 8
What type of motor is commonly used to rotate to exact angles?
  1. Induction motor
  2. Servo motor
  3. Universal motor
  4. Shunt motor
Your answer (1-4, or h for hint): abc
  Please type a number, not text. Try again.
Your answer (1-4, or h for hint): 9
  That number is not an option. Choose between 1 and 4.
Your answer (1-4, or h for hint): h
  Hint: Often used in robot arms and RC cars.
Your answer (1-4): 2
  Correct! (half a mark because you used a hint)

Question 2 of 8
What is the total resistance of 10 ohms and 10 ohms in series?
  1. 5 ohms
  2. 10 ohms
  3. 20 ohms
  4. 100 ohms
Your answer (1-4, or h for hint): 1
  Wrong. The correct answer was: 20 ohms

...

=== RESULTS ===
Score: 1.5 / 8
Percentage: 18.8%
Keep studying. You'll get there!

--- Review of your mistakes ---
Q: What is the total resistance of 10 ohms and 10 ohms in series?
   You chose: 5 ohms
   Correct:   20 ohms
```

## My own twist
I added two extra features that were not in the project description, plus one small bonus:
1. **Hint system:** on any question the user can type `h` to see a hint. The hint can only be used once per question, and it has a cost: if the user then answers correctly, they get half a mark (0.5) instead of a full mark. This makes the user think before asking for help and makes the score fairer.
2. **Review of mistakes:** at the end of the quiz, the program lists every question the user got wrong, the answer they chose and the correct answer. This turns the quiz into a study tool because the user can see exactly what to revise. If the user gets everything right, the program says it was a perfect run.
3. **Random order:** the questions are shuffled each time, so the user cannot just memorise the order of the answers.

## What I learned
- How to check user input with `try/except` and `int()` so the program does not crash when someone types a letter instead of a number. I found out that I must always assume the user can type anything.
- How to use functions that return values (`get_choice` and `get_grade`) to keep my code organised and avoid repeating the same code.
- How to store related data in lists (questions, options, answers, hints) where the same index belongs to the same question, and how to use a list of lists for the options.
- How to combine a `while` loop, a `for` loop and `if/elif/else` decisions to control the flow of a program.
- How to use the `random` module to shuffle questions, and how to use comments to explain my code so others can understand it.
- How to put a project on GitHub and write a README so other people can understand and run my work.

## Author
IDONUAGBE GRACE, ND2 MECHATRONICS DEPARTMENT, YABATECH.
