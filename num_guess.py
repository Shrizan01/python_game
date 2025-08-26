import random

print("Welcome to the Number Guessing Game!")
Name = input("What is your name? ").strip()

max_attempts = 10 

while True:  
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print(f"\nAlright {Name}, I have picked a new number between 1 and 100. Let's start!\n")


    while not guessed and attempts < max_attempts:
        guess = input(f"Attempt {attempts + 1}/{max_attempts}: Take a guess: ").strip()

        if not guess.isdigit():
            print("Please enter a valid number.\n")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number_to_guess:
            print("Your guess is too low.\n")
        elif guess > number_to_guess:
            print("Your guess is too high.\n")
        else:
            guessed = True
            print(f"🎉 Congratulations, {Name}! You've guessed the number {number_to_guess} in {attempts} attempts.\n")

 
    if not guessed:
        print(f"😢 Sorry, {Name}. You've used all {max_attempts} attempts.")
        print(f"The number was {number_to_guess}. Better luck next time!\n")

 
    replay = input("Do you want to play again? (yes/no): ").strip().lower()
    if replay not in ["yes", "y"]:
        print("\nThank you for playing! Goodbye! 👋")
        break
