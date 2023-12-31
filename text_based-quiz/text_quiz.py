# Define the questions and choices
questions = [
    {"question": "What is the name of the capital city of France?",
     "choices": ["A. Paris", "B. London", "C. Rome", "D. Lome"],
     #  The correct answer
     "answer": "A"
     },
    {"question": "Which planet is known as the red planet?",
     "choices": ["A: Mars", "B: Venus", "C: Pluto", "D: Jupiter"],
     #  The correct answer
     "answer": "A"
     },
    {"question": "Which keyword is used to define a function in Python?",
     "choices": ["A: def", "B: function", "C: define", "D: func"],
     #  the correct answer
     "answer": "A"
     },
    {
        "question": "What is the result of the following code?\n\nx = 5\ny = 2\nprint(x // y)",
        "choices": ["A. 2", "B. 2.5", "C. 2.0", "D. 2.2"],
        # the correct answer
        "answer": "A"
    },
    {"question": "What is the output of the following code?\nx = 10\ny = 3\nprint(x % y)",
     "choices": ["A. 1", "B. 2", "C. 3", "D. 4"],
     "answer": "A"
     }

]

# Create a function to present the questions and collect user answers.


def run_quiz(questions):
    score = 0
    total_questions = len(questions)  # Get the total number of questions
    for question in questions:
        print(question["question"])
        for choice in question["choices"]:
            print(choice)
        answer = input("Enter your answer (A, B, C, or D): ")
        if answer.upper() == question["answer"]:
            score += 1
    return score, total_questions  # Return both the score and total questions


# Calculate the score and total questions based on the user's answers.
quiz_score, total_questions = run_quiz(questions)

# Display the actual score as a fraction over the total number of questions administered.
score_fraction = f"{quiz_score}/{total_questions}"
print("Your score is:", score_fraction)
