from random import choice
playing = False
working = True
while working == True:
    cpu = choice(['rock', 'paper', 'scissors'])
    p = input('Enter hand choice (rock, paper, scissors or say stop): ')
    while playing == False:
        if p in {'rock', 'paper', 'scissors'}:
            playing = True
        elif p == 'stop':
            working = False
            playing = False
    if p == cpu:
        print(f"CPU: {p}. It is a tie")
    else:
        if p == 'rock':
            if cpu == 'scissors':
                print("CPU: Scissors. You win")
            else:
                print("CPU: Paper. You lose")
        elif p == 'scissors':
            if cpu == 'rock':
                print("CPU: Rock. You lose")
            else:
                print("CPU: Paper. You win")
        else: 
            if cpu == 'rock':
                print("CPU: Rock. You win")
            else: 
                print("CPU: Scissors. You lose")
    playing = False



