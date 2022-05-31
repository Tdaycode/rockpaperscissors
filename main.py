import random
print("GAME \nTITLE: ROCK PAPER SCISSORS GAME(RPS) \nROCK-R \nPAPER-P \nSCISSORS-S \n------------------------------------------------------ \n INSTRUCTIONS: \n1. Enter your choice \n2. Then the computer will choose a random choice \n3. Then the winner will be displayed \n4. The game will continue until you enter 'q' to quit")
print("-------------------------------------------------------")
print('GAME RULES\n1. Rock beats Scissors \n2. Scissors beats Paper \n3. Paper beats Rock')

play = True
while play:
    user_choice = input('Enter your choice: ').upper()
    if user_choice != "R" and "P" and "S":
        print('Invalid choice. Please try again')
        continue
    if user_choice == 'q':
        print('Thank you for playing')
        play = False
    else:
        comp_choice = random.choice(['R', 'P', 'S'])
        print(f"Player({user_choice}) : CPU({comp_choice})")
        if user_choice == comp_choice:
            print('It is a tie')
        elif user_choice == 'R' and comp_choice == 'S':
            print('You win')
            play = False
        elif user_choice == 'R' and comp_choice == 'P':
            print('computer wins')
            play = False
        elif user_choice == 'P' and comp_choice == 'R':
            print('You win')
            play = False
        elif user_choice == 'P' and comp_choice == 'S':
            print('computer wins')
            play = False
        elif user_choice == 'S' and comp_choice == 'P':
            print('You win')
            play = False
        elif user_choice == 'S' and comp_choice == 'R':
            print('computer wins')
            play = False
