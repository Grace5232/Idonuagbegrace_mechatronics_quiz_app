# Mechatronics Quiz App
# A short multiple-choice quiz with scoring, hints and a review of mistakes.

import random  # used to shuffle the order of the questions

# ---------- QUESTION DATA (stored in lists) ----------
# Each list uses the same position (index) for the same question.
questions = [
    "What does a resistor do in a circuit?",
    "Which unit is used to measure electrical current?",
    "Which component is used to turn a motor on and off with a small signal?",
    "What does PLC stand for?",
    "Which sensor measures how far away an object is without touching it?",
    "What is the formula for Ohm's law?",
    "What type of motor is commonly used to rotate to exact angles?",
    "What is the total resistance of 10 ohms and 10 ohms in series?",
]

# Each question has 4 options (a list inside a list)
options = [
    ["Stores charge", "Limits current flow", "Generates voltage", "Amplifies signals"],
    ["Volt", "Ohm", "Ampere", "Watt"],
    ["Relay", "Resistor", "Fuse", "Capacitor"],
    ["Power Line Controller", "Programmable Logic Controller",
     "Primary Load Circuit", "Pulse Level Converter"],
    ["Ultrasonic sensor", "Strain gauge", "Thermocouple", "Potentiometer"],
    ["V = I x R", "P = V / I", "R = V x I", "I = R / V"],
    ["Induction motor", "Servo motor", "Universal motor", "Shunt motor"],
    ["5 ohms", "10 ohms", "20 ohms", "100 ohms"],
]

# The correct option number (1 to 4) for each question
answers = [2, 3, 1, 2, 1, 1, 2, 3]

# Hints for each question (used in my own twist)
hints = [
    "Think about the word 'resist'.",
    "Named after a French physicist, André-Marie ...",
    "It is an electrically operated switch.",
    "It is used a lot in factory automation.",
    "It sends out sound waves above human hearing.",
    "Voltage equals current multiplied by something.",
    "Often used in robot arms and RC cars.",
    "In series, you simply add the values.",
]


# ---------- FUNCTIONS ----------
def get_choice(number_of_options, hint_allowed):
    """Keep asking until the user gives a valid answer.
    Returns an int (the chosen option) or the letter 'h' (hint request)."""
    while True:  # loop until we get valid input
        text = input("Your answer (1-" + str(number_of_options) + (", or h for hint): " if hint_allowed else "): ")).strip().lower()

        # Hint requested (only allowed once per question)
        if text == "h" and hint_allowed:
            return "h"

        # Try to convert the input to a whole number
        try:
            choice = int(text)
        except ValueError:
            print("  Please type a number, not text. Try again.")
            continue

        # Check the number is within range
        if 1 <= choice <= number_of_options:
            return choice
        print("  That number is not an option. Choose between 1 and " + str(number_of_options) + ".")


def get_grade(percentage):
    """Return a grade and message based on the final percentage."""
    if percentage >= 80:
        return "Excellent! You think like an engineer."
    elif percentage >= 60:
        return "Good job! A little more practice and you'll master it."
    elif percentage >= 40:
        return "Fair attempt. Review the topics you missed."
    else:
        return "Keep studying. You'll get there!"


def run_quiz():
    """Run the quiz and return the final score and the list of mistakes."""
    score = 0.0
    missed = []  # list that stores the questions the user got wrong

    # Shuffle the question order so each attempt is different
    order = list(range(len(questions)))
    random.shuffle(order)

    # Loop through each question
    for number, i in enumerate(order, start=1):
        print("\nQuestion " + str(number) + " of " + str(len(questions)))
        print(questions[i])
        for position, option in enumerate(options[i], start=1):
            print("  " + str(position) + ". " + option)

        hint_used = False
        choice = get_choice(len(options[i]), True)

        # TWIST: the user may ask for a hint, but it costs half a mark
        if choice == "h":
            print("  Hint: " + hints[i])
            hint_used = True
            choice = get_choice(len(options[i]), False)

        # Check the answer
        if choice == answers[i]:
            if hint_used:
                score += 0.5
                print("  Correct! (half a mark because you used a hint)")
            else:
                score += 1
                print("  Correct! +1")
        else:
            correct_text = options[i][answers[i] - 1]
            print("  Wrong. The correct answer was: " + correct_text)
            missed.append([questions[i], options[i][choice - 1], correct_text])

    return score, missed


# ---------- MAIN PROGRAM ----------
print("=== Mechatronics Quiz ===")
print("Answer by typing the option number. Type h for a hint (costs half a mark).")

final_score, missed_questions = run_quiz()
percentage = final_score / len(questions) * 100

print("\n=== RESULTS ===")
print("Score: " + str(final_score) + " / " + str(len(questions)))
print("Percentage: " + str(round(percentage, 1)) + "%")
print(get_grade(percentage))

# TWIST: show a review of every question the user got wrong
if len(missed_questions) > 0:
    print("\n--- Review of your mistakes ---")
    for item in missed_questions:
        print("Q: " + item[0])
        print("   You chose: " + item[1])
        print("   Correct:   " + item[2])
else:
    print("\nPerfect run, nothing to review!")
