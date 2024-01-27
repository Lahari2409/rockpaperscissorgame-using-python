import random

options = ("rock", "paper", "scissors")

running = True #special keyword (1)

while running:#True(1) #False(0)

    player = None
    computer = random.choice(options)

    while player not in options:#True
        player = input("Enter a choice (rock, paper, scissors): ")

    print("Player: {}".format(player))
    print("Computer: {}".format(computer))

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")
