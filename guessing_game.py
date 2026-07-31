#Number guessing game
#Player has 3 attempts to guess the number

play_again = "yes"
import random
while play_again == "yes":

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    print("You have 3 attempts")

    
    secret_num = random.randint(1,100)
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts = attempts+1
        if guess < 1 or guess > 100:
            print("Enter a number between 1 and 100")
            
        elif guess < secret_num:
            print("Too Low!")
            if attempts < max_attempts:
                print(f"attempts left: {max_attempts - attempts}")
        elif guess > secret_num:
            print("Too High!")
            if attempts < max_attempts:
                print(f"attempts left: {max_attempts - attempts}")
        else:
            print("Correct!")
            break
    if guess != secret_num:
        print(f"Game over! The correct number was {secret_num}.")

    play_again = input("Do you want to play again? (yes/no): ").lower() 
print("Thanks for playing!")