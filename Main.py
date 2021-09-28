import random

ver = 0
human = 0
computer = 0
while (ver == 0):
    player = int(input("1 - Stone, 2 - Paper, 3 - Scissors \n" ))
    if (((player == 1) or (player == 2)) or (player == 3)):
            ver = 1 
    if (player == 1):
        print("You choose Stone")
    if (player == 2):
        print("You choose Paper")
    if (player == 3):
        print("You choose Scissors")
    comp = random.randint(1, 3)
    if comp == 1:
        print("Computer choose Stone") 
    if comp == 2:
        print("Computer choose Paper")
    if comp == 3:
        print("Computer choose Scissors")
    if (player == comp):
        win = 0
    if ((player == 1) and (comp == 2)):
        win = 2 
    if ((player == 1) and (comp == 3)):
        win = 1 
    if ((player == 2) and (comp == 1)):
        win = 1  
    if ((player == 2) and (comp == 3)):
        win = 2 
    if ((player == 3) and (comp == 1)):
        win = 2
    if ((player == 3) and (comp == 2)):
        win = 1
    if (win == 0):
        print("Neech!")
    if (win == 1):
        print("Win Human!")
        human = human + 1
    if (win == 2):
        print("Win Computer!")
        computer = computer + 1
    print("Let's congratulate the winner, and let's start all over again. May the best man win!")
    print("human score ",human,":",computer, "computer score")
    ver = 0
