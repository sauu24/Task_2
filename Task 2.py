import random

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)

attempts = 0
print("Welcome to the Guessing Game!")
print("I have selected a number between 1 and 100. Can you guess it?")

while True:
    try:
        # Take input from the user
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Check if the guess is too high, too low, or correct
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
    except ValueError:
        print("Invalid input! Please enter a valid number.")