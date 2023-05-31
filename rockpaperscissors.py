import random

options = ['rock', 'paper', 'scissors']

choices = options[:]



## Which option beats which.
def thinker (ply, comp):
    #print("player", ply, options.index(ply))
    #print("computer", comp, options.index(comp))
    result = options.index(ply) - options.index(comp)
    result = result % 3
    #print(choices)
    if result == 1:
        choices.append(options[(options.index(ply) + 1) % 3])
        choices.remove(comp)
    elif result == 2:
        choices.append(comp)
    return result # 1 = player W, 2 = player L, 0 = tie


## Playing rules
print("Let's play Rock/Paper/Scissors!")
print("Rock beats Scissors, Paper beats rock, Scissors beats paper.")

while True:
    ## Randomly choose one
    compchoice = random.choice(choices)

    ## Get input.
    plychoice = ""
    while plychoice not in options:
        plychoice = input("rock, paper or scissors? ")
        plychoice = plychoice.lower()

    #print("Computer", compchoice, "Player", plychoice)
    goal = thinker(plychoice, compchoice)
    print("Computer played: ", compchoice)
    print("You played: ", plychoice)
    
    ##results
    if goal == 0:
        print("You tied.")
    elif goal == 1:
        print("You won!!!")
    elif goal == 2:
        print("You lose..")
    else:
        print("You have broken Rock, Paper & Scissors by going above 2 or below 3.")
