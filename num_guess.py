user_input = int(input("Enter the integer for the player to guess."))

guess = int(input("Enter your guess."))

count_guesses = 1

while guess != user_input:
    if guess > user_input:
        print("Too high - try again:")
    else:
        print("Too low - try again:")
    guess = int(input())
    count_guesses += 1
if count_guesses == 1:
    print("You guessed it in 1 try.")
else:
    print("You guessed it in", count_guesses, "tries.")

#please work :(