import random

while True:
    choice = input("Heads or Tails? ").lower()
    flip = random.randint(0, 1)

    if choice == "heads" and flip == 0:
        print("You win!")
    elif choice == "tails" and flip == 1:
        print("You win!")
    elif choice == "heads" and flip == 1:
        print("You lose!")
    elif choice == "tails" and flip == 0:
        print("You lose!")
    else:
        print("Invalid input")
    play_again = input("Play again? (y/n) ").lower()
    if play_again == "n":
        break
    else:
        continue
