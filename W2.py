#TASK 2
import random
def guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
        
    attempts = 0
    
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        user_guess = input("Take a guess: ")
        
        if user_guess.lower() == "quit":
            print("Okay, the number was {}.".format(number_to_guess))
            break
        
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("That's not a valid number!")
            continue
        
        attempts += 1
        
        if user_guess == number_to_guess:
            print("Congratulations! You found the number in {} attempts.".format(attempts))
            break
        elif user_guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    guessing_game()