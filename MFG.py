print("...rock...\n...paper...\n...scissors...")
a=input("enter Players 1's choice : ")
if a:
    for x in range(1,100):
        print("******No cheating########")
    b=input("enter Players 2's choice: ")
    if b:
        if (a=="rock" or a=="scissors" or a=="paper") and (b=="rock" or b=="scissors" or b=="paper") :
            print('Boom')
        if a==b:
            print('Tied')
        elif a=="rock" and b=="paper":
            print('Player 2 wins')
        elif (b=="rock" and a=="paper"):\
            print('Player 1"s wins')
        elif a=="scissors" and b=="paper":
            print("Player 1's wins")
        elif (b=="scissors" and a=="paper"):
            print("Players 2's win")
        elif a=="scissors" and b=="rock":
            print("Players Players 2's win")
        elif (b=="scissors" and a=="rock"):
            print("Player 1's wins")
    else:
        print('Enter Correct Value')
else:
     print('Enter your choice to proceed')
delay=input('Press enter to quit')
exit()
