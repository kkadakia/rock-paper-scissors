print("Rock Paper Scissors ---- SHOOT")
import random
import time
import os

done = False

wins, loss, ties = 0, 0, 0

names = {'R': 'rock', 'P': 'paper', 'S': 'scissors'}
loses = {'R': 'P', 'P': 'S', 'S': 'R'}

def clear_screen():
    """ Clears the screen. Works for both Windows and Unix systems. """
    os.system('cls' if os.name == 'nt' else 'clear')


def print_hand(hand):
    """ Prints the hand representation based on the choice. """
    if hand == "rock":
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    elif hand == "paper":
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    elif hand == "scissors":
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")


def animate_choices(player_choice, computer_choice):
    """ Animates both player and computer choices. """
    for _ in range(3):
        for hand in ["rock", "paper", "scissors"]:
            print("Your choice:")
            print_hand(hand)
            print("\nComputer's choice:")
            print_hand(hand)
            time.sleep(0.2)
            clear_screen()
    print("Final Choices:")
    print("Your choice:")
    print_hand(player_choice)
    print("\nComputer's choice:")
    print_hand(computer_choice)
    

done = False
wins, loss, ties = 0, 0, 0
choice_map = {"R": "rock", "P": "paper", "S": "scissors"}
loses = {"R": "P", "P": "S", "S": "R"} # Mapping of what each choice loses to

while not done:
    choices = input('Please chose your next move (R, P, S) (Q to quit): ').upper()
    if choices == 'Q':
        done = True
        continue
    elif choices not in ['R', 'P', 'S']:
        print("Invalid Command")
        continue

    cpu_choice = random.choice(['R', 'P', 'S'])
    animate_choices(choice_map[choices], choice_map[cpu_choice])

    if choices == cpu_choice:
        print(f"It is a tie! You both choose {choice_map[choices]}")
        ties += 1
    else:
        if cpu_choice == loses[choices]:
            print(f"SallyGoose4 Wins! Harry Potter chose {choice_map[choices]}, SallyGoose4 chose {choice_map[cpu_choice]}")
            loss += 1
        else:
            print(f"Harry Potter Wins! You chose {choice_map[choices]}, SallyGoose4 chose {choice_map[cpu_choice]}")
            wins += 1
    
    print(f"\nCurrent Stats: {wins} Wins, {loss} Loss, {ties} Ties")
    print("\n") # Extra space for next round

