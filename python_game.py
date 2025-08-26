
print("Welcome to my Quiz Game!")
name = input("Enter your name: ")
print("Hello", name, "! Let's start the quiz.")

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["a) Berlin", "b) Madrid", "c) Paris", "d) Rome"],
        "answer": "c"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["a) 10", "b) 12", "c) 11", "d) 15"],
        "answer": "b"
    },
    {
        "question": "Which language is this program written in?",
        "options": ["a) Java", "b) C++", "c) Python", "d) Ruby"],
        "answer": "c"
    }
]
score = 0
for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)
    print()

    answer = input("Your answer: ").lower()  # get user input
    if answer == q["answer"]:      # check if answer is correct
        print("Correct! ✅\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is {q['answer']}.\n")
        
print(f"Quiz finished! {name}, your final score is {score}/{len(questions)} 🎉")