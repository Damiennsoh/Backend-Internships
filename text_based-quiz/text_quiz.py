# Define the questions and choices
questions = [
    {"question": "What is the name of the capital city of France?",
     "choices": ["A. Paris", "B. London", "C. Rome", "D. Rome"],
    #  The correct answer
     "answer": "A"
    },
    {"question": "Which planet is known as the red planet?",
     "choices": ["A: Mars", "B: Venus", "C: Pluto", "D: Jupiter"],
    #  The correct answer
    "answer": "A"
    },
    {"question":"Which keyword is used to define a function in Python?",
     "choices": ["A: def", "B: function", "C: define", "D: func"],
    },
    {
    "question": "What is the result of the following code?\n\nx = 5\ny = 2\nprint(x // y)",
    "choices": ["A. 2", "B. 2.5", "C. 2.0", "D. 2.2"],
    "answer": "A"
    },

    ]

# Create a function to present the questions and collect user answers.
def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["question"])
        for choice in question["choices"]:
            print(choice)
        answer = input("Enter your answer (A, B, C, or D): ")
        if answer.upper() == question["answer"]:
            score += 1
    return score

# Calculate the score based on the user's answers.
quiz_score = run_quiz(questions)

# Display results of ansers
print("Your score is:", quiz_score)
