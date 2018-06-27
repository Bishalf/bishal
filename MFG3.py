print("...rock...\n...paper...\n...scissors...")
a = input("Players 1's choice : ")
if a:
    for x in range(1, 100):
        print("******No cheating########")
    b = input("Players 2's choice: ")
    if b:
        if (a == "rock" or a == "scissors" or a == "paper") and (b == "rock" or b == "scissors" or b == "paper"):
            print('Boom')
        if a == b:
            print('Tied')
        elif a == "rock":
            if b == "paper":
                print("Player 2 wins")
            elif b == "scissors":
                print("Player 1 wins")
        elif a == "paper":
            if b == "rock":
                print("Player 1 wins")
            elif b == "scissors":
                print("Player 2 wins")
        elif a == "scissors":
            if b == "paper":
                print("Player 1 wins")
            elif b == "rock":
                print("Player 2 wins")
    else:
        print('Enter Correct Value')
else:
    print('Enter your choice to proceed')
delay = input('Press enter to quit')
exit()
