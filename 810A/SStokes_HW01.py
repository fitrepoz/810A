import random

#player is set to empty value to start
player = '' 

#if the user picks q or quit then the game will end
while player != 'q': 

    #let user know the choices and take user input
    print('Select your choice: r for rock, r for paper, s for scissor, or q to quit')
    player = input('')

    #automatically set player input to lowercase if uppercase is used
    player = player.lower()

    #available choices for user to select
    choices = 'rps'

    #if player enters q or quit program stops
    if player == 'q':
        break

    #if user input is not in the choices up above error merssage is displayed
    if player not in choices:
        print('Not a choice, please try again!')
        continue
    player = choices.find(player)

    #computer gets randomized answer, out of 3 options
    comp = random.randrange(0, 3)
    choice = comp

    choices = ['rock', 'paper', 'scissor']

    #based on selection choice is displayed
    print('Computer picked:', choices[comp])

    #logic to determine if player wins, loses or ties based on input
    if player == 0 and comp == 2:
        print('You win! :) \n')
    elif player == 2 and comp == 0:
        print('You lose! :( \n')
    elif player > comp:
        print('You win! :) \n')
    elif player < comp:
        print('You lose! :( \n')
    elif player == comp:
        print('You tied!\n')