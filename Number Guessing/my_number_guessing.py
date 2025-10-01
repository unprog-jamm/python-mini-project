import random

random_number = random.randint(1, 10) # Generate a random number between 1 and 100

attempts = 0 # number of attempts made

while attempts < 5: # while attempts are less than 5, if else, player loses

    attempts += 1
    print("Attempt", attempts, "of 5")

    guess = int(input("Guess the random number between 1 and 10!: ")) #player tries to guess the number
    if guess < random_number:
        print("Too low! Try again.")
        
    elif guess > random_number:
        print("Too high! Try again.")

    else:
        print(f"Congratulations! You've guessed the number {random_number} correctly in {attempts} attempt/s.")
        break


if attempts == 5:
    print(f"You have used all of your attempts! the number was {random_number}. Better luck next time!")


