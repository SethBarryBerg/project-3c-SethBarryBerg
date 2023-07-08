user_input = int(input("Enter the integer for the player to guess."))
print("")

guess = int(input("Enter your guess."))
print("")

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

#added prints to try to make it work in gradescope >:(