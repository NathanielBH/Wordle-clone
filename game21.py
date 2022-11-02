#playing blackjack against the conmputer
#author: Nathaniel Borrok-Hoffman
import random

#simulates the rolling of two dice

#prompts user to ask if they want to roll
def get_response():
    play = input("do you want to roll again? y/n: ")
    if play != 'y':
        play = False
    else:
        play = True
    while play == True:
        return play

#main tracks the state of the game
def main():
    play = input('do you want to play? y/n: ')
#simulates the rolling of two dice
    while play == 'y':
        dice1 = dice_roll()
        dice2 = dice_roll()
        compdice1 = dice_roll()
        compdice2 = dice_roll()
        dice_total= dice1+dice2
        compdice_total = compdice1+compdice2
        print(f' your total roll is: {dice_total}')
        cont = get_response()
        while cont and dice_total < 21:
            score2 = dice_roll()
            compscore2 = dice_roll()
            dice_total += score2
            compdice_total += compscore2
            print(f'your score is {dice_total}')
            if dice_total < 21:
                cont = get_response()
        print(f'Computer has a score of {compdice_total}')
        print(f'Your score is {dice_total}')
        if (compdice_total > 21 and dice_total > 21) or (compdice_total == dice_total):
            print("YOU TIED")
        elif (compdice_total > dice_total) and compdice_total<= 21:
            print('You lost loser sucker idiot')
        else:
            print('You win you georgeous person')
        play = input('Do you want to play again? y/n: ')      

def dice_roll():
    dice1 = random.randint(1, 6)

    return dice1
main()
