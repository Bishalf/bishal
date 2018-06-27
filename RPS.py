import random
ml=["rock","paper","scissors"]
b=random.choice(ml)
a = input("Players 1's choice : ").lower()
if a:
    if (a == "rock" or a == "scissors" or a == "paper") :
        if a==b:
            print("Computer plays:",b)
            print("Tie")
        elif a == "rock":
            if b == "paper":
                print("Computer plays:",b)
                print("Computer wins")
            elif b == "scissors":
                print("Computer plays:",b)
                print("Player 1 wins")
        elif a == "paper":
            if b == "rock":
                print("Computer plays:",b)
                print("Player 1 wins")
            elif b == "scissors":
                print("Computer plays:",b)
                print("Computer wins")
        elif a == "scissors":
            if b == "paper":
                print("Computer plays:",b)
                print("Player 1 wins")
            elif b == "rock":
                print("Computer plays:",b)
                print("Computer wins")
    else:
        print("Enter correct Value")
else:
    print('You Forget to add your choice')
delay = input('Press enter to quit')
exit()
