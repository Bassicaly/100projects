import random

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player_choice < 0 or player_choice > 2:
    print("Invalid choice. You lose!")
    exit()

computer_choice = random.randint(0, 2)

rps = ["Rock", "Paper", "Scissors"]

print(f"You chose: {rps[player_choice]}")
print(f"Computer chose: {rps[computer_choice]}")

if player_choice == computer_choice:
    print("It's a draw.")
elif player_choice == 0 and computer_choice == 2:
    print(f"You win. {rps[player_choice]} beats {rps[computer_choice]}.")
elif player_choice == 1 and computer_choice == 0:
    print(f"You win. {rps[player_choice]} beats {rps[computer_choice]}.")
elif player_choice == 2 and computer_choice == 1:
    print(f"You win. {rps[player_choice]} beats {rps[computer_choice]}.")
else:
    print(f"You lose. {rps[computer_choice]} beats {rps[player_choice]}.")