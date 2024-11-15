# Number guessing game
winning_number = 42
guess = 1 
number = int(input("Guess a number between 1 and 99: "))
game_over = False

while not game_over:
    if number == winning_number:
        print("Correct! ")
        break
    else:
        if number < winning_number:
            print("Too low!")
            guess += 1
            number = int(input("Guess again: "))
        else:
            print("Too High!")
            guess += 1
            number = int(input("Guess again: "))